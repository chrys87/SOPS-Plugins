# Example usage:
# echo "This is a test." | socat - UNIX-CLIENT:/tmp/orca-PID.sock
# Where PID is orca's process id.
# Prepend text to be spoken with <!#APPEND#!> to make it not interrupt, for inaccessible windows.

import select, socket, os, os.path
from threading import Thread

# Orca
import orca.braille
import orca.orca
import orca.speech
import orca.settings

APPEND_CODE = '<!#APPEND#!>'

def outputMessage(Message):
	# Prepare
	append = Message.startswith(APPEND_CODE)
	if append:
		Message = Message[len(APPEND_CODE):]
	# Speak
	if (orca.settings.enableSpeech):
		if not append:
			speechserver = orca.speech._speechserver
			speechserver._cancel()
		if Message != '':
			orca.speech.speak(Message)
	# Braille
	if (orca.settings.enableBraille):
		orca.braille.displayMessage(Message)

def voiceWatchDog():
    socketFile = '/tmp/orca-' + str(os.getppid()) + '.sock'
    if os.path.exists(socketFile):
        os.unlink(socketFile)
    orcaSock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    orcaSock.bind(socketFile)
    os.chmod(socketFile, 0o222)
    orcaSock.listen(1)
    while True:
        # Check if the client is still connected and if data is available:
        try:
            r, _, _ = select.select([orcaSock], [], [], 0.8)
        except select.error:
            break
        if r == []:
            continue
        if orcaSock in r:
            client_sock, client_addr = orcaSock.accept()
        try:
            rawdata = client_sock.recv(8129)
        except:
            pass
        try:
            data = rawdata.decode("utf-8").rstrip().lstrip()
            outputMessage(data)
        except:
            pass
        try:
            client_sock.close()
        except:
            pass
    if orcaSock:
        orcaSock.close()
        orcaSock = None
    if os.path.exists(socketFile):
        os.unlink(socketFile)

t = Thread(target=voiceWatchDog)
t.start()
