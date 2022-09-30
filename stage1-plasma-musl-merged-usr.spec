subarch: amd64
target: stage1
version_stamp: openrc-plasma-musl-merged-usr-2022.09.30
rel_type: default
profile: local:plasma-musl-merged-usr
snapshot: 2022.09.30
source_subpath: default/stage3-amd64-openrc-latest
compression_mode: pixz
update_seed: yes
update_seed_command: --update --deep --newuse @world
portage_confdir: /tmp/portage_tmp_confdir
portage_overlay: /var/db/repos/local
#portage_confdir: @REPO_DIR@/releases/portage/stages
#portage_prefix: releng
