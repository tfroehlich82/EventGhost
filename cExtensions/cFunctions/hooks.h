/*
// This file is part of the EventGhost project.
//
// Copyright (C) 2005-2008 Lars-Peter Voss <bitmonster@eventghost.org>
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301 USA
*/

#include "Python.h"
#define _WIN32_WINNT 0x501
#include <windows.h>


extern void 
AwakeWaitThread(void);

extern PyObject *
ResetIdleTimer(PyObject *self, PyObject *args);

extern PyObject *
SetIdleTime(PyObject *self, PyObject *args);

extern PyObject *
StartHooks(PyObject *self, PyObject *args);

extern PyObject *
StopHooks(PyObject *self, PyObject *args);


