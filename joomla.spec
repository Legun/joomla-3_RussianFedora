#
# spec file for package joomla
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
%define		apache_serverroot /var/www/html/%{name}

Name:           joomla
Version:        3.3.3
Release:        1
Summary:        Web Content management system (CMS)
Group:		Productivity/Publishing/HTML/Tools
License:        GPL-2.0
URL:            http://www.joomla.org/
Source0:        http://joomlacode.org/gf/download/frsrelease/19665/160049/Joomla_3.3.3-Stable-Full_Package.zip
BuildArch:      noarch
Requires:	php php-mysql php-gd php-mbstring php-json php-zlib php-zip
Recommends:	httpd
Suggests:	mysql

%description
Joomla is an award-winning content management system (CMS), which enables
you to build Web sites and powerful online applications. Many aspects,
including its ease-of-use and extensibility, have made Joomla the most
popular Web site software available. Best of all, Joomla is an open
source solution that is freely available to everyone.



%prep
%setup -q -c


%build


%install
%{__mkdir} -p ${RPM_BUILD_ROOT}%{apache_serverroot}
%{__cp} -r * ${RPM_BUILD_ROOT}%{apache_serverroot}/




%files
%defattr(-,root,root)
%dir %{apache_serverroot}
%{apache_serverroot}/*


%changelog
* Thu Jul 19 2012 on@morlock.nu
- Upstream version 2.5.6
- Initial package
