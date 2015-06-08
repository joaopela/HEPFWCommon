#!/bin/bash 

# Job parameters
JOB_DO_JOBLOG=
JOB_DO_CPULOG=
JOB_DO_MEMLOG=

# CMSSW Parameters
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

if [ "$JOB_DO_CPULOG" = "TRUE" ]; then
  cat /proc/cpuinfo |& tee $CMSSW_JOB_CFG.cpu.log
fi

if [ "$JOB_DO_MEMLOG" = "TRUE" ]; then
  cat /proc/meminfo |& tee $CMSSW_JOB_CFG.mem.log
fi

# Making job status
rm -f $CMSSW_JOB_CFG.status.*
touch $CMSSW_JOB_CFG.status.running

echo "Job start time: $(date)"

if [ "$JOB_DO_JOBLOG" = "TRUE" ]; then
  cmsRun $CMSSW_JOB_CFG.py |& tee $CMSSW_JOB_CFG.job.log
  CMSSW_OUTPUT_CODE=${PIPESTATUS[0]}

else
  cmsRun $CMSSW_JOB_CFG.py
  CMSSW_OUTPUT_CODE=$?
fi

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
