Summary:	FSF Emacs compatibility files
Summary(pl):	Pliki dla kompatybilno∂ci z FSF Emacsem
Name:		xemacs-fsf-compat-pkg
%define 	srcname	fsf-compat
Version:	1.10
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Group(cs):	Aplikace/Editory/Emacs
Group(da):	Programmer/Tekstbehandlere/Emacs
Group(de):	Applikationen/Editoren/Emacs
Group(es):	Aplicaciones/Editores/Emacs
Group(fr):	Applications/Editeurs/Emacs
Group(is):	Forrit/Ritlar/Emacs
Group(it):	Applicazioni/Editor/Emacs
Group(ja):	•¢•◊•Í•±°º•∑•Á•Û/•®•«•£•ø/Emacs
Group(no):	Applikasjoner/Editorer/Emacs
Group(pl):	Aplikacje/Edytory/Emacs
Group(pt):	AplicaÁıes/Editores/Emacs
Group(ru):	“…Ãœ÷≈Œ…—/Ú≈ƒ¡À‘œ“Ÿ/Emacs
Group(sl):	Programi/Urejevalniki/Emacs
Group(sv):	Till‰mpningar/Editorer/Emacs
Group(uk):	“…ÀÃ¡ƒŒ¶ “œ«“¡Õ…/Ú≈ƒ¡À‘œ“…/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs

%description
FSF Emacs compatibility files.

%description -l pl
Pliki dla kompatybilno∂ci z FSF Emacsem.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages

gzip -9nf lisp/fsf-compat/README lisp/fsf-compat/ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc lisp/fsf-compat/README.gz lisp/fsf-compat/ChangeLog.gz 
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.elc
