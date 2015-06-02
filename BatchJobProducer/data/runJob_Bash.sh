#!/bin/bash 

JOB_DIR=
JOB_NAME=

# Setting core file size to zero
ulimit -c 0

cd $JOB_DIR

cat /proc/cpuinfo |& tee $CMSSW_JOB_CFG.cpu.log
cat /proc/meminfo |& tee $CMSSW_JOB_CFG.mem.log

# Making job status
rm -f $JOB_NAME.status.*
touch $JOB_NAME.status.running

echo "Job start time: $(date)"
COMMAND
JOB_EXIT_CODE=$?
echo "Job end time: $(date)"

if [ $JOB_EXIT_CODE -eq 0 ]; then 
  # Updating job status
  rm -f $JOB_NAME.status.*
  touch $JOB_NAME.status.done
else
  # Updating job status
  rm -f $JOB_NAME.status.*
  touch $JOB_NAME.status.failed_cmssw_$JOB_EXIT_CODE
fi

exit $JOB_EXIT_CODE
