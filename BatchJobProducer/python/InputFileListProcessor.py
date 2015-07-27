class InputFileListProcessor:

  def __init__(self):
    self.inputFiles = list()
  
  def getFromDAS(self,dataset):

    import subprocess
    import tempfile

    # query DAS
    myQuery = 'das_client.py --limit=0 --query="file dataset='+str(dataset)+'"'
    
    #print myQuery
    
    outF = tempfile.TemporaryFile()
    errF = tempfile.TemporaryFile()
    
    proc = subprocess.Popen(myQuery,shell=True,stdout=outF,stderr=errF)
    proc.wait() # wait for the process to terminate otherwise the output is garbled
    
    outF.seek(0) # rewind to the beginning of the file
    errF.seek(0) # rewind to the beginning of the file
    
    self.inputFiles = outF.read().splitlines()

  def dump_CMSSW_cfi(self,fileName):
    
    outFile = open(fileName,'w');

    outFile.write("import FWCore.ParameterSet.Config as cms\n");
    outFile.write("\n")
    outFile.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n");
    outFile.write("readFiles = cms.untracked.vstring()\n");
    outFile.write("secFiles  = cms.untracked.vstring()\n");
    outFile.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n");
    outFile.write("readFiles.extend( [\n");
    
    count=1
    
    for f in self.inputFiles:
      outFile.write("       '"+f);
      
      if count % 254==0:
        outFile.write("\n");
        outFile.write("       ] );\n");
        outFile.write("readFiles.extend( [\n");
      else:
        outFile.write(",\n");
      
      count=count+1
    
    outFile.write("       ] );\n");
    outFile.write("secFiles.extend([])\n");
