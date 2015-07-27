class InputFileListProcessor:

  def __init__(self):
    
    self.inputFiles = list()
    self.outputDir  = ""
    self.nJobs      = 1
    self.listFormat = 'cmssw'
    self.nFiles     = 0
    
  
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
    self.nFiles     = len(self.inputFiles)

    outF.close()
    errF.close()

  def dump_CMSSW_cfi(self,fileName,filelist):
    
    outFile = open(self.outputDir+"/"+fileName,'w');

    outFile.write("import FWCore.ParameterSet.Config as cms\n");
    outFile.write("\n")
    outFile.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n");
    outFile.write("readFiles = cms.untracked.vstring()\n");
    outFile.write("secFiles  = cms.untracked.vstring()\n");
    outFile.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n");
    outFile.write("readFiles.extend( [\n");
    
    count=1
    
    for f in filelist:
      outFile.write("       '"+f+"'");
      
      if count % 254==0:
        outFile.write("\n");
        outFile.write("       ] );\n");
        outFile.write("readFiles.extend( [\n");
      elif count==len(filelist):
        outFile.write("\n");
      else:
        outFile.write(",\n");
      
      count=count+1
    
    outFile.write("       ] );\n");
    outFile.write("secFiles.extend([])\n");

  def splitByNumberOfJobs(self,nJobs):

    if self.nFiles<nJobs:
      print "Number of jobs is bigger than number of input files... setting number of jobs to number of files"
      nJobs=self.nFiles

    filesPerJob = float(self.nFiles) / float(nJobs)
    print "Making Jobs "+str(nJobs)+" ("+str(filesPerJob)+" files per job)"

    fileIndex = 0
    for x in range(0,nJobs):

      jobInputFiles = list()

      while fileIndex < (x+1)*filesPerJob:
        jobInputFiles.append(self.inputFiles[fileIndex])
        fileIndex=fileIndex+1

      self.dump_CMSSW_cfi("inputSrc_job"+str(x+1)+"_cfi.py",jobInputFiles)


  def splitByNumberOfFiles(self,filesPerJob):
    
    if self.listFormat=='cmssw':
      
      jobs=[self.inputFiles[x:x+filesPerJob] for x in xrange(0, len(self.inputFiles), filesPerJob)]
      
      jobNumber=1;
      for j in jobs:
        self.dump_CMSSW_cfi("inputSrc_job"+str(jobNumber)+"_cfi.py",j)
        jobNumber=jobNumber+1

