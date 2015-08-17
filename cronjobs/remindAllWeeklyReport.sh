#!/bin/bash
BASEDIR=$(dirname $0)
#QACHAT='d45f5b0998b5e501099dc47765ef8a0b'
#SHINGCHAT='0d223d3f39325511e5695cffe6e36b31'

CHATS=(
  'd45f5b0998b5e501099dc47765ef8a0b'
)

#$BASEDIR/send.sh $QACHAT '工作辛苦了，記得訂明天便當 https://dinbendon.net/do/'

for CHAT in ${CHATS[@]} 
do
  $BASEDIR/send.sh $CHAT "$(python $BASEDIR/remindAllWeeklyReport.py)"
done

