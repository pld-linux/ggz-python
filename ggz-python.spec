# TODO:
# - register client *.dsc in /etc/ggz.modules
# - ggzdmod?
# - subpackages? (client/games, server, python-* with client/server modules?)
Summary:	GGZ Gaming Zone - Python libraries and Games
Summary(pl.UTF-8):	GGZ Gaming Zone - biblioteki i gry w Pythonie
Name:		ggz-python
Version:	0.0.14.1
Release:	0.1
License:	LGPL v2.1+
Group:		Applications/Games
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0103b0a6a95623109625212ccf1137ef
Patch0:		%{name}-rsvg.patch
Patch1:		%{name}-install.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	ggz-client-libs-devel >= 0.0.14
BuildRequires:	libggz-devel >= 0.0.14
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.234
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For people not liking C or C++, the GGZ Python package provides
everything they need to start hacking on GGZ.

Players will love the elegance and flexibility of games written in a
scripting language.

#%description -l pl.UTF-8

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%{__aclocal}
%{__autoconf}
%configure \
	ggzd_confdir=%{_sysconfdir}/ggzd
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{_libdir}/ggz-python
%py_ocomp $RPM_BUILD_ROOT%{_libdir}/ggz-python
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%find_lang ggzpython

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ggzpython.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README README.GGZ
# games/clients
%attr(755,root,root) %{_bindir}/escape-sdl
%attr(755,root,root) %{_bindir}/ggzboard
%attr(755,root,root) %{_bindir}/vibora
%attr(755,root,root) %{_bindir}/xadrez-chines
%attr(755,root,root) %{_libdir}/ggz/goclient
%attr(755,root,root) %{_libdir}/ggz/goclient.helper
%dir %{_libdir}/ggz-python
%{_libdir}/ggz-python/common
%{_libdir}/ggz-python/ggzboard
%{_libdir}/ggz-python/xadrez-chines
%{_datadir}/ggz/ggzboard
%{_datadir}/ggz/vibora
%{_datadir}/ggz/xadrez-chines
%{_desktopdir}/escape-sdl.desktop
%{_desktopdir}/ggzboard.desktop
%{_desktopdir}/vibora.desktop
%{_desktopdir}/xadrez-chines.desktop
%{_mandir}/man6/escape-sdl.6*
%{_mandir}/man6/ggzboard.6*
%{_mandir}/man6/vibora.6*
%{_mandir}/man6/xadrez-chines.6*
# servers
%dir %{_sysconfdir}/ggzd
%dir %{_sysconfdir}/ggzd/games
%{_sysconfdir}/ggzd/games/goserver.dsc
%{_sysconfdir}/ggzd/games/server_checkers.dsc
%{_sysconfdir}/ggzd/games/server_hnefatafl.dsc
%{_sysconfdir}/ggzd/games/server_ludo.dsc
%{_sysconfdir}/ggzd/games/xadrez-chines-server.dsc
%dir %{_sysconfdir}/ggzd/rooms
%{_sysconfdir}/ggzd/rooms/goserver.room
%{_sysconfdir}/ggzd/rooms/server_checkers.room
%{_sysconfdir}/ggzd/rooms/server_hnefatafl.room
%{_sysconfdir}/ggzd/rooms/server_ludo.room
%{_sysconfdir}/ggzd/rooms/xadrez-chines-server.room
%attr(755,root,root) %{_libdir}/ggzd/goserver
%attr(755,root,root) %{_libdir}/ggzd/server_checkers.py
%attr(755,root,root) %{_libdir}/ggzd/server_hnefatafl.py
%attr(755,root,root) %{_libdir}/ggzd/server_ludo.py
%attr(755,root,root) %{_libdir}/ggzd/xadrez-chines-server
# python-ggz*
%attr(755,root,root) %{py_sitedir}/ggzchess.so
%attr(755,root,root) %{py_sitedir}/ggzcoresimple.so
%attr(755,root,root) %{py_sitedir}/ggzmod.so
%attr(755,root,root) %{py_sitedir}/rsvgsdl.so
%{py_sitedir}/ggzsettings.py[co]
%{py_sitedir}/sdlnewstuff.py[co]
%{py_sitedir}/GGZChess-0.1-py*.egg-info
%{py_sitedir}/GGZCore-0.1-py*.egg-info
%{py_sitedir}/GGZMod-0.3-py*.egg-info
%{py_sitedir}/RSVGSDL-0.1-py*.egg-info
