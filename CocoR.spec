Summary:	Parser and lexer generator
Summary(pl):	Generator analizatorów leksykalnych i sk³adniowych
Name:		CocoR
Version:	1.50
Release:	1
Group:		Development/Tools
License:	unknown
Source0:	ftp://cs.ru.ac.za/pub/coco/cocorc15.tgz
# Source0-md5:	843dcb81ac549931f5437f143a15349c
Patch0:		%{name}-compile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coco/R generator.

%description -l pl
Generator analizatorów leksykalnych i sk³adniowych Coco/R.

%prep
%setup -q -c
%patch0 -p1

%build
export CRFRAMES=`pwd`/frames
uudecode dos2unix.uue
chmod +x dos2unix.sh
./dos2unix.sh unix.mk
%{__make} -f unix.mk dos2unix OPTFLAGS="%{rpmcflags}"
%{__make} -f unix.mk linux OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_datadir}/coco/frames/cplus2}

install cocor $RPM_BUILD_ROOT%{_bindir}

cp -f frames/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames
cp -f frames/cplus2/*.frm $RPM_BUILD_ROOT%{_datadir}/coco/frames/cplus2

install docs/cocor.1 $RPM_BUILD_ROOT%{_mandir}/man1/cocor.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/cocor
%{_mandir}/man1/cocor.1*
%dir %{_datadir}/coco
%{_datadir}/coco/frames
