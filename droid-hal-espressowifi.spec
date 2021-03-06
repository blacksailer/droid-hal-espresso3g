# These and other macros are documented in dhd/droid-hal-device.inc

%define device espressowifi
%define vendor samsung

%define vendor_pretty Samsung
%define device_pretty Galaxy Tab 2 WiFi

%define installable_zip 1
%define enable_kernel_update 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
