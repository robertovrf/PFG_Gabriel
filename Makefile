# Variables
DNC=dnc . -v
DN=dana

.DEFAULT_GOAL: all
.PHONY: all server client distributor constant readn writen readn-writen

all: server client distributor constant readn writen readn-writen

server:
	@echo ">> Compiling server..."
	@cd server/ && $(DNC)
	@echo "Server compiled!"

client:
	@echo ">> Compiling client..."
	@cd client/ && $(DNC)
	@echo "Client compiled!"

distributor:
	@echo ">> Compiling distributor..."
	@cd distributor/ && $(DNC)
	@echo "Distributor compiled!"

constant:
	@echo ">> Compiling constant..."
	@cd constant/ && $(DNC)
	@echo "Constant compiled!"	

readn:
	@echo ">> Compiling readn..."
	@cd readn/ && $(DNC)
	@echo "Readn compiled!"	

writen:
	@echo ">> Compiling writen..."
	@cd writen/ && $(DNC)
	@echo "Writen compiled!"	

readn-writen:
	@echo ">> Compiling readn-writen..."
	@cd readn-writen/ && $(DNC)
	@echo "Readn-Writen compiled!"	

clean:
	@echo ">> Cleaning up..."
	find . -name '*.o' -delete
	@echo "All executables removed!"