Summary:	Lexer for wide encodings
Summary(pl):	Lexer dla du¿ych kodowañ znaków
Name:		ocaml-wlex
Version:	20021107
Release:	1
License:	LGPL
Group:		Development/Tools
Vendor:		Alain Frisch <Alain.Frisch@ens.fr>
URL:		http://www.eleves.ens.fr/home/frisch/soft/
# Source0-md5:	7a934e7158464632872647bad6f1145d
Source0:	http://www.eleves.ens.fr/home/frisch/info/wlex-%{version}.tar.gz
Patch0:		%{name}-lex-src.patch
BuildRequires:	ocaml >= 3.04-7
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lexer generator for wide encodings (like UTF8) and the associated
runtime system. This package contains files needed to run bytecode
executables using this library.

%description -l pl
Generator lekserów dla du¿ych kodowañ znaków (jak UTF8) oraz system
uruchomieniowy. Pakiet ten zawiera binaria potrzebne do uruchamiania
programów u¿ywaj±cych tej biblioteki.

%package devel
Summary:	Lexer for wide encodings - development part
Summary(pl):	Lexer dla du¿ych kodowañ znaków - cze¶æ programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
Lexer generator for wide encodings (like UTF8) and the associated
runtime system. Lexer generator is covered by QPL (as it was derived
from part of OCaml), runtime system is covered by LGPL. This package
contains files needed to develop OCaml programs using this library.

%description devel -l pl
Generator lekserów dla du¿ych kodowañ znaków (jak UTF8) oraz system
uruchomieniowy. Generator jest rozpowszechniany na licencju QPL (jako
¿e jest on bazowany na czê¶ci OCamla), system uruchomieniowy natomiast
jest rozpowszechiany na zasadach LGPL. Pakiet ten zawiera pliki
niezbêdne do tworzenia programów u¿ywaj±cych tej biblioteki.

%prep
%setup -q -n wlex-%{version}
%patch0 -p1

%build
%{__make} wlex runtime

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{site-lib/wlexing,stublibs}}

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}

mv -f $RPM_BUILD_ROOT%{_libdir}/ocaml/wlexing/META \
	$RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/wlexing/
echo 'directory = "+wlexing"' >> $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/wlexing/META

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -r test/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(644,root,root,755)
%doc README RELEASE *.mli
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/ocaml/wlexing
%{_libdir}/ocaml/wlexing/*.cm[ixa]*
%{_libdir}/ocaml/wlexing/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/wlexing
