Summary:	Parser and lexer generator
Summary(pl):	Generator analizatorów leksykalnych i sk³adniowych
Name:		CocoR
Version:	1.50
Release:	1
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
License:	Unknown
Source0:	ftp://cs.ru.ac.za/pub/coco/cocorc15.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coco/R generator.

%description -l pl
Generator analizatorów leksykalnych i sk³adniowych Coco/R.

%prep
%setup -q -c

%build
export CRFRAMES=`pwd`/frames
uudecode dos2unix.uue
chmod +x dos2unix.sh
./dos2unix.sh unix.mk
%{__make} -f unix.mk dos2unix CFLAGS="$RPM_OPT_FLAGS -I../cplus2"
%{__make} -f unix.mk linux CFLAGS="$RPM_OPT_FLAGS -I../cplus2"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/coco/frames/cplus2}

install -s cocor $RPM_BUILD_ROOT%{_bindir}

cp frames/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames/
cp frames/cplus2/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames/cplus2

install docs/cocor.1 $RPM_BUILD_ROOT%{_mandir}/man1/cocor.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/cocor
%{_mandir}/man1/cocor.1*
%{_datadir}/coco/frames
