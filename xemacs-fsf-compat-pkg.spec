### Comment
# This file is modified automatically by 'xemacs-adapter' script
# from PLD-project CVS repository: cvs.pld.org.pl, module SPECS
# For more details see comments in this script
### EndComment

Summary: 	FSF Emacs compatibility files.
Summary(pl):	FSF Emacs compatibility files.

Name:    	xemacs-fsf-compat-pkg
%define 	srcname	fsf-compat
Version: 	1.07
Release:	1

### Preamble
License:	GPL
Group:    	Applications/Editors/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
URL:      	http://www.xemacs.org
Source:   	ftp://ftp.xemacs.org/packages/%{srcname}-%{version}-pkg.tar.gz
BuildRoot:	/tmp/%{name}-%{version}-root
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires: 	xemacs
### EndPreamble

%description


%description -l pl 


### Main
%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
gzip -9nf lisp/fsf-compat/README lisp/fsf-compat/ChangeLog 

%clean
rm -fr $RPM_BUILD_ROOT
### EndMain

### PrePost
### EndPrePost

### Files
%files
%defattr(644,root,root,755)
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
%doc lisp/fsf-compat/README.gz lisp/fsf-compat/ChangeLog.gz 
### EndFiles
