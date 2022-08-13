An attempt at packaging haproxy_exporter
----------------------------------------

Just a personal experiment.

```
spectool -g haproxy_exporter.spec
fedpkg --name haproxy_exporter --release rawhide local
fedpkg --name haproxy_exporter --release rawhide scratch-build  --srpm --target rawhide --arches x86_64
```

While this works, it should be useless when working with haproxy 2.x, and deploying
using containers should be preferable anyway.

Also, this does not rebuild the exporter.
See how it is done on the [node exporter][1].

Local build and [koji][2] scratch builds look to work. RPMs are not signed.

TODO: find a way to make Copr build work.

[1]: https://src.fedoraproject.org/rpms/golang-github-prometheus-node-exporter/tree/rawhide
[2]: https://koji.fedoraproject.org/koji/taskinfo?taskID=90756771
