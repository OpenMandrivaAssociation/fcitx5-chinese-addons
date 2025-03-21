Name:		fcitx5-chinese-addons
Version:	5.1.8
Release:	1
Source0:	https://github.com/fcitx/fcitx5-chinese-addons/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	http://download.fcitx-im.org/data/py_stroke-20121124.tar.gz
Source2:	http://download.fcitx-im.org/data/py_table-20121124.tar.gz
Summary:	Chinese input system addons for fcitx
URL:		https://github.com/fcitx/fcitx5-chinese-addons
License:	LGPL-2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Fcitx5Config)
BuildRequires:	cmake(Fcitx5Core)
BuildRequires:	cmake(Fcitx5Qt6WidgetsAddons)
BuildRequires:	cmake(Fcitx5Utils)
BuildRequires:	cmake(Fcitx5ModuleLuaAddonLoader)
BuildRequires:	cmake(LibIMECore)
BuildRequires:	cmake(LibIMEPinyin)
BuildRequires:	cmake(LibIMETable)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(OpenCC)
BuildRequires:	cmake(fmt)
BuildRequires:	boost-devel
BuildRequires:	gettext
BuildSystem:	cmake

%description
Chinese input system addons for fcitx

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Requires: %{name} = %{EVRD}

%description devel
Development files for %{name}

%prep -a
cp %{S:1} %{S:2} modules/pinyinhelper

%files -f %{name}.lang
%{_bindir}/scel2org5
%{_libdir}/fcitx5/*.so
%{_libdir}/fcitx5/qt6/libcustomphraseeditor.so
%{_libdir}/fcitx5/qt6/libpinyindictmanager.so
%{_datadir}/fcitx5/addon/*.conf
%{_datadir}/fcitx5/chttrans/gbks2t.tab
%{_datadir}/fcitx5/inputmethod/*.conf
%{_datadir}/fcitx5/lua/imeapi/extensions/pinyin.lua
%{_datadir}/fcitx5/pinyin
%{_datadir}/fcitx5/pinyinhelper
%{_datadir}/fcitx5/punctuation
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.ChineseAddons.metainfo.xml

%files devel
%{_includedir}/Fcitx5/Module/fcitx-module/*
%{_libdir}/cmake/Fcitx5Module*
