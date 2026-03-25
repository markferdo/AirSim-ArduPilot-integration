# AirSim Setup Documentation (Windows)

## 1. Introduction

This document describes the complete process of installing and setting up Microsoft AirSim on a Windows system using Unreal Engine and Visual Studio. The goal of this setup is to create a working drone simulation environment that can later be integrated with external controllers such as ArduPilot.

---

## 2. Software Requirements

The following software components were required:

* Microsoft AirSim
* Unreal Engine 4.27.2
* Visual Studio 2026 (with C++ support)
* Git
* Python (optional, for API usage)

---

## 3. Installation and Setup Process

### 3.1 Installing Visual Studio 2026

Visual Studio was installed with the following components:

* Desktop Development with C++
* MSVC v143 (VS 2022 C++ build tools)
* Windows 10 SDK (10.0.19041 or newer)
* CMake tools for Windows

These components are required to compile AirSim’s C++ code.

---

### 3.2 Cloning AirSim Repository

The AirSim repository was cloned using Git into a non-system drive (E:) to avoid permission issues:

```bash
git clone https://github.com/Microsoft/AirSim.git
cd AirSim
```

Installation was intentionally avoided on the C: drive to prevent script failures and administrator permission issues.

---

### 3.3 Building AirSim

The build process was initiated using:

```bash
build.cmd
```

This step:

* Downloaded required dependencies
* Compiled AirSim source code
* Generated plugin files for Unreal Engine

The output plugin was created in:

```
AirSim\Unreal\Plugins\AirSim
```

---

### 3.4 Resolving Build Issues

#### Issue 1: Missing v143 Toolset

Error:

```
Platform Toolset 'v143' not found
```

Solution:
Installed MSVC v143 toolset via Visual Studio Installer.

---

#### Issue 2: Unreal Engine Compatibility

Initially, Unreal Engine 5 was installed, which caused compatibility issues.

Solution:
Installed Unreal Engine 4.27.2, which is fully supported by AirSim.

---

#### Issue 3: Unreal Project File Generation Failure

The build process failed at generating `.uproject` files due to missing Unreal registry entries.

Solution:

* Opened the project manually using Unreal Editor
* Bypassed UnrealVersionSelector issues
* Allowed Unreal to generate and compile required modules

---

### 3.5 Opening the AirSim Environment

The simulation project was opened using:

```
E:\AirSimProjects\AirSim\Unreal\Environments\Blocks\Blocks.uproject
```

Upon opening:

* Unreal detected missing modules
* The system prompted to rebuild
* The AirSim plugin was compiled successfully

---

### 3.6 Running the Simulation

After successful compilation:

1. The Blocks environment was loaded
2. The simulation was started using the "Play" button in Unreal Engine
3. The AirSim environment became operational

---

## 4. System Architecture

The setup consists of three main components:

* Unreal Engine: Provides physics simulation and rendering
* AirSim: Acts as the simulation interface and vehicle model
* Visual Studio: Compiles AirSim C++ code

---

## 5. Current Status

At the end of this setup:

* AirSim is successfully built and integrated with Unreal Engine
* The Blocks environment loads correctly
* The simulation runs without errors
* The system is ready for further integration (e.g., Python API or ArduPilot)

---

## 6. Conclusion

The AirSim environment was successfully installed and configured on a Windows system. Several issues were encountered, including missing toolchains and Unreal Engine compatibility problems, but they were resolved through proper configuration and troubleshooting. The system is now ready for simulation and further development.

---
