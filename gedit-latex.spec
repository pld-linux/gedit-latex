Summary:	GEdit plugin providing features to ease the edition of LaTeX documents
Summary(pl.UTF-8):	Wtyczka GEdita udostępniająca funkcje ułatwiające edycję dokumentów w LaTeXu
Name:		gedit-latex
Version:	46.2.2
Release:	2
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	https://download.gnome.org/sources/gedit-latex/46/%{name}-%{version}.tar.xz
# Source0-md5:	bfb3bc1d81b89eaa19678a8c549ab833
URL:		https://git.gnome.org/browse/gedit-latex/
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	gedit-devel >= 3.30
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	libpeas-devel >= 1.14.1
BuildRequires:	meson >= 0.50
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gedit >= 3.30
Requires:	glib2 >= 1:2.26.0
Requires:	libpeas >= 1.14.1
Requires:	python3-dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# just python inside, but plugin path is arch-dependent
%define		_enable_debug_packages	0

%description
GEdit plugin providing features to ease the edition of LaTeX
documents.

%description -l pl.UTF-8
Wtyczka GEdita udostępniająca funkcje ułatwiające edycję dokumentów w
LaTeXu.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang gedit-latex

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gedit-latex.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README
%{_libdir}/gedit/plugins/latex.plugin
%dir %{_libdir}/gedit/plugins/latex
%{_libdir}/gedit/plugins/latex/*.py
%{_libdir}/gedit/plugins/latex/bibtex
%{_libdir}/gedit/plugins/latex/latex
%{_libdir}/gedit/plugins/latex/preferences
%{_libdir}/gedit/plugins/latex/tools
%dir %{_libdir}/gedit/plugins/latex/util
%attr(755,root,root) %{_libdir}/gedit/plugins/latex/util/eps2png.pl
%{_datadir}/gedit/plugins/latex
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml
