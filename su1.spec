#
# Note:
#    Feel free to bump to "1", but first check possibility security holes in
#    default settings (i don't know if there are or not)
#
Summary:	Allows specified users to run certain commands as root
Summary(pl):	Umo¿liwia wykonywaniew poleceñ jako root dla konkretnych u¿ytkowników
Name:		su1
Version:	5.1
Release:	0.1
Epoch:		0
License:	distributable
Group:		Applications/System
Source0:	http://canb.auug.org.au/~dbell/programs/%{name}-%{version}.tar.gz
# Source0-md5:	da913f453c334b38ca767bb2dac3b3da
#Source1:	%{name}.pamd
#Source2:	%{name}.logrotate
Patch0:		%{name}-Makefile.patch
URL:		http://canb.auug.org.au/~dbell/programs/
BuildRequires:	pam-devel
#BuildRequires:	libselinux-devel
Requires:	pam >= 0.77.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/pam.d,/var/{log,cache},%{_mandir}/man1,%{_bindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT/var/log/su1
mv su1.priv{,.sample}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README su1.priv.sample
%attr(0400,root,root) %verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/su1.priv
%attr(0600,root,root) %config(noreplace) %verify(not size mtime md5) /etc/pam.d/su1
%attr(4555,root,root) %{_bindir}/su1
%{_mandir}/man*/*
%attr(0600,root,root) %ghost /var/log/su1
#%%attr(0640,root,root) /etc/logrotate.d/*
%attr(0600,root,root) %dir /var/cache/su1
