U='r'
S=input
R=open
J='path.txt'
F=True
C=str
A=print
import os as E,sys
def D(path):
	O='Restarting Program!';N='Deleting path.txt';M='VRising Path Does Not Exist!';K=path;G='/6 Found!';F='File ';B=0;A('Running Path Validation...')
	if E.path.exists(K):
		for (P,Q,L) in E.walk(K):
			for D in L:
				if D=='start_server_example.bat':B=B+1;A(F+C(B)+G)
				elif D=='config.vdf':B=B+1;A(F+C(B)+G)
				elif D=='VRisingServer.exe':B=B+1;A(F+C(B)+G)
				elif D=='UnityCrashHandler64.exe':B=B+1;A(F+C(B)+G)
				elif D=='steamclient.dll':B=B+1;A(F+C(B)+G)
				elif D=='licenses.txt':B=B+1;A(F+C(B)+G)
		if B==6:A('All Files Found!');H(K)
		elif B<=5 and B>=3:A('Not All Files Found - Results May Vary!')
		else:A(M);A(N);E.remove(J);A(O);I()
	else:A(M);A(N);E.remove(J);A(O);I()
def I():
	try:C=R(J,U);B=C.read();C.close();D(B);H(B)
	except FileNotFoundError:
		while F:
			A('My Path For Example: E:/SteamLibrary/steamapps/common/VRisingDedicatedServer/');B=S('Please Enter Your Path To VRising Dedicated Server: ')
			if B=='':A('Invalid Path')
			else:C=R(J,'w');C.write(B);C.close();break
		D(B);H(B)
def H(path):
	X=False;O=path;N='Line Number: ';M='\nFull Line String Was Mentioned: ';L='In File: ';T=[];G=[];H=C(S('Enter the text you want to search for: '))
	for (V,Y,W) in E.walk(O):
		for K in W:
			if K.endswith('.txt')or K.endswith('.log')or K.endswith('.json')or K.endswith('.info'):T.append(E.path.join(V,K))
	I=X
	for D in T:
		P=R(D,U,encoding='utf8');J=P.readlines()
		for B in J:
			if H in B:I=F;G.append(D);A(L+D+M+B+N+C(J.index(B)))
			elif H.upper()in B:I=F;G.append(D);A(L+D+M+B+N+C(J.index(B)))
			elif H.lower()in B:I=F;G.append(D);A(L+D+M+B+N+C(J.index(B)))
			elif H.capitalize()in B:I=F;G.append(D);A(L+D+M+B+N+C(J.index(B)))
			elif H.title()in B:I=F;G.append(D);A(L+D+M+B+N+C(J.index(B)))
	if I==X:A('No Results With Search Query!');P.close();Q(O)
	else:A("Total Files Containing Your Query '"+H+"': "+C(len(G)));P.close();Q(O)
def Q(path):
	D='Invalid Input!'
	while F:
		try:
			B=C(S('Would you like to search again? (y/n): ')).upper()
			if B=='Y':A('Restarting Search!');H(path)
			elif B=='N':A('Exiting VRising Text Scraper!');A('Made With Love By InfamyStudio~CortexCode');sys.exit()
			else:A(D)
		except ValueError:A(D)
if __name__=='__main__':B=I()