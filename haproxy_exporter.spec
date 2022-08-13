Name:    haproxy_exporter
Version: 0.13.0
Release: 1%{?dist}
Summary: haproxy_exporter

License: Apache-2.0 license
Source0: https://github.com/prometheus/haproxy_exporter/releases/download/v%{version}/haproxy_exporter-%{version}.linux-amd64.tar.gz
Source1: haproxy_exporter.service

%description
haproxy_exporter


%install
mkdir -p -m0755 %{buildroot}/usr/bin/ %{buildroot}/etc/systemd/system/
tar -zvf %{SOURCE0}  --directory=%{buildroot}/usr/bin/ --strip-components=1 -x haproxy_exporter-%{version}.linux-amd64/haproxy_exporter 
cp %{SOURCE1} %{buildroot}/etc/systemd/system/haproxy_exporter.service

%files
/usr/bin/haproxy_exporter
/etc/systemd/system/haproxy_exporter.service

%post
mkdir -p /var/lib/private/haproxy_exporter

%changelog
* Sat Aug 13 2022 <rigault.francois@gmail.com> 
- Initial Build.
