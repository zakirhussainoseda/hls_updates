cd
echo "************* pip - Installation  **************"
sudo apt install python3-pip --assume-yes

echo "************* MyHDL - Installation  *************"
pip install myhdl

echo "************* MyHDL - Updation  ****************"
pip install --upgrade myhdl

cd
echo "************ Yosys Open SYnthesis Suite - Installation  **************"
echo "************  Installing yosys dependancies ***************************"
echo
echo
sudo apt-get install build-essential clang bison flex \
	libreadline-dev gawk tcl-dev libffi-dev git \
	graphviz xdot pkg-config python3 libboost-system-dev \
	libboost-python-dev libboost-filesystem-dev zlib1g-dev --assume-yes
	
cd
echo
echo
echo "************* Cloning yosys and will start installation of yosys ******************"
echo
echo
cd
cd
git clone https://github.com/YosysHQ/yosys.git
cd yosys
sudo make
sudo make install
cd
cd
cd
echo "******************* openSTA installation ***********************"
cd 
echo
echo
echo "******************* Cloning OpenSTA and will start installation of OpenSTA *****************"
echo
echo
cd
cd
git clone https://github.com/The-OpenROAD-Project/OpenSTA.git
cd OpenSTA
mkdir build
cd build
sudo apt install cmake --assume-yes
sudo apt-get update -y --assume-yes
sudo apt-get install -y swig --assume-yes
cmake ..
sudo make
sudo make install
cd
cd
echo
echo
##Install Icarus iverilog
echo "************** Installing iverilog ******************"
echo
echo
sudo apt-get install -y iverilog --assume-yes
echo "*************** Installing gtkwave *******************"
echo
echo
sudo apt install gtkwave --assume-yes
cd
cd
echo "**************************************************************************************"
echo "                             Installation Completed                                   "
echo "**************************************************************************************"
echo