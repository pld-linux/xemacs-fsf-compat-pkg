Summary:	FSF Emacs compatibility files
Summary(pl):	Pliki dla kompatybilno¶ci z FSF Emacsem
Name:		xemacs-fsf-compat-pkg
%define 	srcname	fsf-compat
Version:	1.11
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs

%description
FSF Emacs compatibility files.

%description -l pl
Pliki dla kompatybilno¶ci z FSF Emacsem.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/fsf-compat/README lisp/fsf-compat/ChangeLog

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/fsf-compat/README.gz lisp/fsf-compat/ChangeLog.gz
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
