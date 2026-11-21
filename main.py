import json,os,urllib.request as U
E=os.getenv("MAKEFUN_ENV_URL")
def ps(p,b):
 return json.load(U.urlopen(U.Request(E+p,data=json.dumps(b).encode())))
V=(0,100,320,330,500,900,0)
P="kkkkkkkklmmiimmlljikkijlkkkookkkllmppmllmmoqqommuuuuuuuukkkkkkkk"
N="aceeeecacgkkkkgcekmnnmkeelnoonleeknoonkeelmnnmlecgkllkgcaceeeeca"
K="eccaacceeccaacceeccaacceeccaaccegeecceegiggggggiookkkkoooqmkkmqo"
PS=("",P,N,N,"k"*64,N,K)
SQ=[i for i in range(128)if not i&136]
KN=(14,31,33,18,-14,-31,-33,-18)
BD=(15,17,-15,-17)
RD=(16,1,-16,-1)
KD=BD+RD
CM=[15]*128
CM[4]=12;CM[116]=3;CM[0]=13;CM[7]=14;CM[112]=7;CM[119]=11
KG=[4,116]
ND=0;NB=4e4;I=1000000
def parse(f):
 global S,C,EP,B
 f=f.split();B=[0]*128;r=7;l=0
 for ch in f[0]:
  if ch=='/':r-=1;l=0
  elif ch.isdigit():l+=int(ch)
  else:
   p="PNBRQK".index(ch.upper())+1;s=r*16+l;B[s]=p if ch.isupper() else -p
   if p==6:KG[ch.islower()]=s
   l+=1
 S=[-1,1][f[1]=='w']
 C=sum(1<<i for i in range(4)if"KQkq"[i]in f[2])
 EP=-1 if f[3]=='-' else (ord(f[3][1])-49)*16+ord(f[3][0])-97
def att(q,by):
 for D,g in(((-by*15,-by*17),1),(KN,2),(KD,6)):
  for d in D:
   t=q+d
   if not t&136 and B[t]==g*by:return 1
 for D,G in((BD,3),(RD,4)):
  for d in D:
   t=q+d
   while not t&136 and not B[t]:t+=d
   if not t&136 and B[t]in(G*by,5*by):return 1
 return 0
def gen(cp=0):
 ms=[];ap=ms.append
 for sq in SQ:
  p=B[sq]
  if p*S<1:continue
  a=p*S
  if a==1:
   d=16*S;t=sq+d
   if not B[t]:
    if not (t>>4)%7:
     for pr in(5,4,3,2):ap((sq,t,pr))
    elif not cp:
     ap((sq,t,0))
     if sq>>4==1+5*(S<0)and not B[t+d]:ap((sq,t+d,0))
   for dd in(d-1,d+1):
    t=sq+dd
    if not t&136 and(B[t]*S<0 or t==EP):
     if not (t>>4)%7:
      for pr in(5,4,3,2):ap((sq,t,pr))
     else:ap((sq,t,0))
  elif a in(2,6):
   for d in KN if a==2 else KD:
    t=sq+d
    if not t&136 and B[t]*S<=0 and(B[t]or not cp):ap((sq,t,0))
   if a==6 and not cp and sq==KG[(1-S)//2]:
    w=4-3*(S>0)
    for bit,sg in((w,1),(2*w,-1)):
     if C&bit and not B[sq+sg]and not B[sq+2*sg]and(sg>0 or not B[sq-3])and not(att(sq,-S)or att(sq+sg,-S)or att(sq+2*sg,-S)):ap((sq,sq+2*sg,0))
  else:
   for d in(BD,RD,KD)[(a>3)+(a>4)]:
    t=sq+d
    while not t&136:
     q=B[t]
     if q:
      if q*S<0:ap((sq,t,0))
      break
     if not cp:ap((sq,t,0))
     t+=d
 return ms
def mk(m):
 global S,C,EP
 f,t,pr=m;p=B[f];c=B[t];cs=-1
 if EP==t and abs(p)<2 and not c:cs=t-16*S;c=B[cs];B[cs]=0
 u=(c,C,EP,cs)
 B[t]=pr*S if pr else p;B[f]=0
 EP=f+16*S if abs(p)<2 and abs(t-f)==32 else -1
 if abs(p)==6:
  KG[(1-S)//2]=t
  if t-f==2:B[f+1]=B[f+3];B[f+3]=0
  if f-t==2:B[f-1]=B[f-4];B[f-4]=0
 C&=CM[f]&CM[t]
 S=-S
 return u
def un(m,u):
 global S,C,EP
 f,t,pr=m;c,C,EP,cs=u;S=-S
 B[f]=S if pr else B[t]
 B[t]=0;B[cs if cs>=0 else t]=c
 if abs(B[f])==6:
  KG[(1-S)//2]=f
  if t-f==2:B[f+3]=B[f+1];B[f+1]=0
  if f-t==2:B[f-4]=B[f-1];B[f-1]=0
def od(ms):
 return sorted(ms,key=lambda m:-(V[m[2]]if m[2]else abs(B[m[1]])*100-abs(B[m[0]])))
def sr(d,a,b,y):
 global ND
 ND+=1
 if ND>NB:raise Exception
 chk=att(KG[(1-S)//2],-S)
 if d<1 and not chk:
  st=0
  for sq in SQ:
   p=B[sq];r=sq>>4
   if p:st+=(V[abs(p)]+(ord(PS[abs(p)][(r if p>0 else 7-r)*8+(sq&7)])-97)*5-50)*((p>0)*2-1)
  st*=S
  if st>=b:return b
  bs=max(a,st)
 else:bs=-I
 n=0
 for m in od(gen(d<1 and not chk)):
  u=mk(m)
  if att(KG[(1+S)//2],S):un(m,u);continue
  n+=1
  s=-sr(d-1,-b,-a,y+1)
  un(m,u)
  bs=max(bs,s);a=max(a,s)
  if a>=b:break
 if not n and(d>0 or chk):return -100000+y if chk else 0
 return bs
def best(fen):
 global ND
 parse(fen);z=None
 for d in range(1,40):
  ND=0;c=z;a=-I
  try:
   for m in od(gen()):
    u=mk(m)
    if att(KG[(1+S)//2],S):un(m,u);continue
    if z is None:z=m
    s=-sr(d-1,-I,I,1);un(m,u)
    if s>a:a=s;c=m
  except:break
  z=c
 return z
if E:
 while 1:
  g=ps("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   try:m=best(g["fen"])
   except:m=None
   mv=None
   if m:
    f,t,pr=m;mv=f"{'abcdefgh'[f&7]}{(f>>4)+1}{'abcdefgh'[t&7]}{(t>>4)+1}"+("nbrq"[pr-2]if pr else"")
   mv=mv or g["legal_moves"][0]
   g=ps("/move",{"game":g["game"],"move":mv})
