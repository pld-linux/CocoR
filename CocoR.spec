Summary:	Parser and lexer generator
Summary(pl):	Generator analizatorów leksykalnych i składniowych
Name:		CocoR
Version:	1.50
Release:	1
Group:		Development/Tools
License:	Unknown
Source0:	ftp://cs.ru.ac.za/pub/coco/cocorc15.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coco/R generator.

%description -l pl
Generator analizatorów leksykalnych i składniowych Coco/R.

%prep
%setup -q -c

%build
export CRFRAMES=`pwd`/frames
uudecode dos2unix.uue
chmod +x dos2unix.sh
./dos2unix.sh unix.mk
%{__make} -f unix.mk dos2unix CFLAGS="%{rpmcflags} -I../cplus2"
%{__make} -f unix.mk linux CFLAGS="%{rpmcflags} -I../cplus2"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/coco/frames/cplus2}

install cocor $RPM_BUILD_ROOT%{_bindir}

cp -f frames/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames/
cp -f frames/cplus2/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames/cplus2

install docs/cocor.1 $RPM_BUILD_ROOT%{_mandir}/man1/cocor.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/cocor
%{_mandir}/man1/cocor.1*
%{_datadir}/coco/frames
