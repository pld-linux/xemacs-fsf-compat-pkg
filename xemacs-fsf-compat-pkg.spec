Summary:	FSF Emacs compatibility files
Summary(pl.UTF-8):   Pliki dla kompatybilności z FSF Emacsem
Name:		xemacs-fsf-compat-pkg
%define 	srcname	fsf-compat
Version:	1.15
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
# Source0-md5:	a68d000cf16b054b20a56e917d57e712
URL:		http://www.xemacs.org/
Requires:	xemacs
Conflicts:	xemacs-sumo
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FSF Emacs compatibility files.

%description -l pl.UTF-8
Pliki dla kompatybilności z FSF Emacsem.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/fsf-compat/README lisp/fsf-compat/ChangeLog
%dir %{_datadir}/xemacs-packages/lisp/fsf-compat
%{_datadir}/xemacs-packages/lisp/fsf-compat/*.el*
