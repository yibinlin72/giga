# -*- coding: UTF-8 -*-

from os.path import join as path_join

# =================================
# basic configuration
# =================================
# 專案路徑
PROJECT_ROOT = "/mnt/d/YB-gigalinktek/Code"

# =================================
# log configuration
# =================================
LOG_ROOT = path_join(PROJECT_ROOT, "logs")
LOG_GL_BACKUP_PATH = path_join(LOG_ROOT, "gl_backup.log")

# =================================
# GitLab Backup Configuration
# =================================

# Official
# GL_BACKUP_LOCAL_PATH = "/volume1/docker/gitlab/gitlab/backups"
# GL_BACKUP_REMOTE_PATH = "/Remote Backup/Gigalink/Gigalink FW"

# Test
GL_BACKUP_LOCAL_PATH = "/mnt/d/YB-gigalinktek/Backup"
GL_BACKUP_REMOTE_PATH = "Remote Backup/Gigalink/Gigalink FW"

