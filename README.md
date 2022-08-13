
```
spectool -g haproxy_exporter.spec
fedpkg --name haproxy_exporter --release rawhide local
fedpkg --name haproxy_exporter --release rawhide scratch-build  --srpm --target rawhide --arches x86_64
```
