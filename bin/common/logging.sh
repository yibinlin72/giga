#!/usr/bin/env bash


function log() {
    echo "$(date +"%Y-%m-%d %H:%M:%S") ${1} ${2}"
}

function info() {
    log "INFO " "${1}"
}

function error() {
    log "ERROR " "${1}"
}

function warning() {
    log "WARNING " "${1}"
}
