#!/usr/bin/env bash
set -e
# =================================================================
cd $(dirname "$0") && cd $(dirname ${PWD}) && cd $(dirname ${PWD})
source bin/common/logging.sh
# =================================================================
info "開始 GitLab異地備份"

if [ "$#" -lt 1 ]; then
    TX_DT=$(date --date='1 days ago' +%Y_%m_%d)
else
    TX_DT=${1}
fi
# echo ${TX_DT}

info "上傳備份檔至 X-LAB Server..."
bash bin/common/python.sh jobs/gl_backup/put_data.py ${TX_DT}

info "完成 GitLab異地備份"
