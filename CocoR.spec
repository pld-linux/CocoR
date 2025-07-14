Summary:	Parser and lexer generator
Summary(pl.UTF-8):	Generator analizatorów leksykalnych i składniowych
Name:		CocoR
Version:	1.17
Release:	1
Epoch:		1
Group:		Development/Tools
License:	Free
Source0:	http://www.scifac.ru.ac.za/coco/cocorc17.tgz
# Source0-md5:	1e2ae1d70ae90f06992e3776cc568a10
Patch0:		%{name}-compile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Coco/R generator.

%description -l pl.UTF-8
Generator analizatorów leksykalnych i składniowych Coco/R.

%prep
%setup -q -c
%patch -P0 -p1

%build
export CRFRAMES=`pwd`/frames
uudecode dos2unix.uue
chmod +x dos2unix.sh
./dos2unix.sh unix.mk
%{__make} -f unix.mk dos2unix \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}"
%{__make} -f unix.mk linux \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}"

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
