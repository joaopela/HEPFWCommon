#!/bin/bash 

CMSSW_DIR=
CMSSW_JOB_DIR=
CMSSW_JOB_CFG=
CMSSW_SCRAM_ARCH=

# Setting core file size to zero
ulimit -c 0

source /afs/cern.ch/cms/cmsset_default.sh
export SCRAM_ARCH=CMSSW_SCRAM_ARCH
cd $CMSSW_DIR
eval `scram runtime -sh`

cd $CMSSW_JOB_DIR

cat /proc/cpuinfo |& tee $CMSSW_JOB_CFG.cpu.log
cat /proc/meminfo |& tee $CMSSW_JOB_CFG.mem.log

# Making job status
rm -f $CMSSW_JOB_CFG.status.*
touch $CMSSW_JOB_CFG.status.running

echo "Job start time: $(date)"

cmsRun $CMSSW_JOB_CFG.py |& tee $CMSSW_JOB_CFG.job.log
CMSSW_OUTPUT_CODE=${PIPESTATUS[0]}
echo $CMSSW_OUTPUT_CODE

echo "Job end time: $(date)"

if [ $CMSSW_OUTPUT_CODE -eq 0 ]; then 
  # Updating job status
  rm -f $CMSSW_JOB_CFG.status.*
  touch $CMSSW_JOB_CFG.status.done
else
  # Updating job status
  rm -f $CMSSW_JOB_CFG.status.*
  touch $CMSSW_JOB_CFG.status.failed_cmssw_$CMSSW_OUTPUT_CODE
fi

exit $CMSSW_OUTPUT_CODE
