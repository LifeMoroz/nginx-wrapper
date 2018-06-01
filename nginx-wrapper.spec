Name: nginx-wrapper
Version: 1.10.0
Release: 1%{?dist}
Summary: Wrapper that provides nginx insted of nginx-rb

License: GPLv2+
URL: http://www.pobox.com/~tranter
Source0: http://www.ibiblio.org/pub/Linux/utils/disk-management/%{name}-%{version}.tar.gz

Requires: nginx = 1.10
Provides: nginx-rb = 1.10

%description
Wrapper that provides nginx insted of nginx-rb


%changelog
* Fri Jun 1 2018 Ruslan Galimov <ruslan.galimov@corp.mail.ru> 
- Initial RPM release
