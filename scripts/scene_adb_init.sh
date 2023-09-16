scene="com.omarea.vtools"
daemon="scene-daemon"

apk=$(pm path $scene)
apk=$(echo ${apk:8})
# unzip
# Extract FILEs from ZIP archive. Default is all files. Both the include and
# exclude (-x) lists use shell glob patterns.
#
# -d DIR  Extract into DIR
# -j      Junk (ignore) file paths
# -l      List contents (-lq excludes archive name, -lv is verbose)
# -n      Never overwrite files (default: prompt)
# -o      Always overwrite files
# -p      Pipe to stdout
# -q      Quiet
# -t      Test compressed data (do not extract)
# -v      List contents verbosely
# -x FILE Exclude files

if [[ ! -f "$apk" ]];then
  echo 'Error: Failed to get the [Scene.apk] file'
  exit -1
fi

cache_dir="/data/local/tmp"

current_process=`pgrep -f $daemon`
if [[ ! "$current_process" == "" ]]; then
  echo 'Kill Current Scene-Daemon >>'
  kill -9 $current_process 2>/dev/null
fi


echo ''
toolkit=$cache_dir/toolkit
mkdir -p $toolkit
# Env PATH add /data/local/tmp
export PATH=$PATH:$toolkit


# Copy [scene-daemon]
if [[ -d /data/local/tmp/res ]]; then
  rm -r /data/local/tmp/res
fi
unzip $apk "*res/raw/daemon" -o -d /data/local/tmp > /dev/null
if [[ -f /data/local/tmp/res/raw/daemon ]]; then
  mv /data/local/tmp/res/raw/daemon $cache_dir/scene-daemon
  chmod 777 $cache_dir/scene-daemon
  rm -r /data/local/tmp/res
  echo 'Success: Copy [scene-daemon] to complete'
else
  echo 'Error: Failed to extract [scene-daemon]!'
  exit 1
fi


# Copy [toybox]
if [[ -d /data/local/tmp/assets ]]; then
  rm -r /data/local/tmp/assets
fi
unzip $apk "*assets/toolkit/toybox-outside64" -o -d /data/local/tmp > /dev/null
if [[ -f /data/local/tmp/assets/toolkit/toybox-outside64 ]]; then
  mv /data/local/tmp/assets/toolkit/toybox-outside64 $toolkit/toybox-outside
  chmod 777 $toolkit/toybox-outside
  rm -r /data/local/tmp/assets
  echo 'Success: Copy [toybox-outside] to complete'
else
  echo 'Error: Failed to extract [toybox-outside]!'
  exit 2
fi

# Copy [busybox]
if [[ -d /data/local/tmp/assets ]]; then
  rm -r /data/local/tmp/assets
fi
unzip $apk "*assets/toolkit/busybox" -o -d /data/local/tmp > /dev/null
if [[ -f /data/local/tmp/assets/toolkit/busybox ]]; then
  mv /data/local/tmp/assets/toolkit/busybox $toolkit/busybox
  chmod 777 $toolkit/busybox
  rm -r /data/local/tmp/assets
  echo 'Success: Copy [busybox] to complete'
else
  echo 'Error: Failed to extract [busybox]!'
  exit 2
fi


echo 'Install BusyBox……'
cd $toolkit
for applet in `./busybox --list`; do
  case "$applet" in
  "sh"|"busybox"|"shell"|"swapon"|"swapoff"|"mkswap")
    echo '  Skip' > /dev/null
  ;;
  *)
    ./busybox ln -sf busybox "$applet";
  ;;
  esac
done
./busybox ln -sf busybox busybox_1_30_1

echo ''
nohup $cache_dir/scene-daemon >/dev/null 2>&1 &
if [[ $(pgrep scene-daemon) != "" ]]; then
  echo 'Scene-Daemon OK! ^_^'
else
  echo 'Scene-Daemon Fail! @_@'
fi

cmd package compile -m speed $scene >/dev/null 2>&1 &

dumpsys deviceidle whitelist +$scene >/dev/null 2>&1
cmd appops set $scene RUN_IN_BACKGROUND allow >/dev/null 2>&1
echo ''
