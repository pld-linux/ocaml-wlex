%define		ocaml_ver	1:3.09.2
Summary:	Lexer for wide encodings
Summary(pl.UTF-8):	Lexer dla dużych kodowań znaków
Name:		ocaml-wlex
Version:	20030827
Release:	19
License:	LGPL
Group:		Development/Tools
URL:		http://www.eleves.ens.fr/home/frisch/soft
# note: no / at the end of URL
Source0:	http://www.eleves.ens.fr/home/frisch/info/wlex-%{version}.tar.gz
# Source0-md5:	4ae79d74436f1004582f8ca12b91ecd9
Patch0:		%{name}-lex-src.patch
Patch1:		%{name}-patch.patch
BuildRequires:	ocaml >= %{ocaml_ver}
BuildRequires:	ocaml-findlib
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lexer generator for wide encodings (like UTF8) and the associated
runtime system. This package contains files needed to run bytecode
executables using this library.

%description -l pl.UTF-8
Generator lekserów dla dużych kodowań znaków (jak UTF8) oraz system
uruchomieniowy. Pakiet ten zawiera binaria potrzebne do uruchamiania
programów używających tej biblioteki.

%package devel
Summary:	Lexer for wide encodings - development part
Summary(pl.UTF-8):	Lexer dla dużych kodowań znaków - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
Lexer generator for wide encodings (like UTF8) and the associated
runtime system. Lexer generator is covered by QPL (as it was derived
from part of OCaml), runtime system is covered by LGPL. This package
contains files needed to develop OCaml programs using this library.

%description devel -l pl.UTF-8
Generator lekserów dla dużych kodowań znaków (jak UTF8) oraz system
uruchomieniowy. Generator jest rozpowszechniany na licencju QPL (jako
że jest on bazowany na części OCamla), system uruchomieniowy natomiast
jest rozpowszechniany na zasadach LGPL. Pakiet ten zawiera pliki
niezbędne do tworzenia programów używających tej biblioteki.

%prep
%setup -q -n wlex-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__make} wlex runtime

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/ocaml/{site-lib/wlexing,stublibs}}

%{__make} install \
	OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%{_libdir}/ocaml \
	INSTALL_BIN=$RPM_BUILD_ROOT%{_bindir}

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
%{_libdir}/ocaml/wlexing/META
%{_libdir}/ocaml/wlexing/*.cm[ixa]*
%{_libdir}/ocaml/wlexing/*.a
%{_examplesdir}/%{name}-%{version}
