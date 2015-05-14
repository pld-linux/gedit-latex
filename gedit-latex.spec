Summary:	GEdit plugin providing features to ease the edition of LaTeX documents
Summary(pl.UTF-8):	Wtyczka GEdita udostępniająca funkcje ułatwiające edycję dokumentów w LaTeXu
Name:		gedit-latex
Version:	3.8.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Editors
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gedit-latex/3.8/%{name}-%{version}.tar.xz
# Source0-md5:	828cb83bb36f12b9aaade82fdca94e09
URL:		https://git.gnome.org/browse/gedit-latex/
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gedit >= 3.8
Requires:	python3-dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GEdit plugin providing features to ease the edition of LaTeX
documents.

%description -l pl.UTF-8
Wtyczka GEdita udostępniająca funkcje ułatwiające edycję dokumentów w
LaTeXu.

%prep
%setup -q

%build
%configure \
	PYTHON=%{__python3} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gedit-latex

%clean
rm -rf $RPM_BUILD_ROOT

%files -f gedit-latex.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{_libdir}/gedit/plugins/latex.plugin
%attr(755,root,root) %{_libdir}/gedit/plugins/latex
%{_datadir}/gedit/plugins/latex
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.latex.gschema.xml
