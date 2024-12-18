
int lo=0,hi=n-1;
int mid= (lo+hi)/2;
int p=n-1;
while(lo<hi){
	if(A[mid]>=A[mid-1] && A[mid]>=A[mid+1]){
		p=mid;
		break;
	}
	else if(A[mid]>=A[mid-1]){
		lo=mid+1;
	}
	else{
		hi=mid-1;
	}
	mid= (lo+hi)/2;
}
return p

-----------------------------
bool present=false;
If(Val>=A[0] && Val<=A[p]) present |= binary_search(A,0,p,Val);
If(Val>=A[n-1] && Val<=A[p]) present |= binary_search_rev(A,p,n-1,Val);
return present;
-----------------------------------
bool isPerfect_Complete_Graph( vector<vector<int>> A ){
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			if(A[i][j]+A[j][i] != 1)return false;
		}
	}

	vector<int> OUT(n,0);

	for(int i=0;i<n;i++){
		int x = row_sum(A[i]); //gives sum of the row
		OUT[x]++;
	}

	for(int i=0;i<n;i++) if(OUT[i]==0)return false;
	return true;
}
---------------------------------------------------
distance(u)= ∞; (initially for all u in V; stores distance from s)
t_finder (G,s,distance,n){
	CreateEmptyQueue(Q);
	distance(s)=0;
	Enqueue(s,Q);
	While(Not IsEmptyQueue(Q)){
		v= Dequeue(Q);
		For each neighbor w of v {
			if(distance(w)== ∞){
				distance(w)=distance(v)+1;
				Enqueue(w,Q);
			}
		}
	}
	max_d=0;
	For u in V {
		max_d= max(max_d,distance(u));
	}
	k=n/3;
	p = min(max_d, 2*k);
	For t in V {
		if(distance(t)==p)return t;
	}
}
---------------------------------------------------
BFS(G, s, t){
	distance(u)= ∞; //initially for all u in V
	CreateEmptyQueue(Q);
	distance(s)=0;
	Enqueue(s,Q);
	While(Not IsEmptyQueue(Q)){
		v= Dequeue(Q);
		For each neighbor w of v {
			if(distance(w)== ∞){
				distance(w)=distance(v)+1;
				Enqueue(w,Q);
			}
		}
	}
	return distance(t);
}

BFS_L(G, s, t){
	parent(u)=-1 //initially for all u in V
	distance(u)= ∞; //initially for all u in V
	CreateEmptyQueue(Q);
	distance(s)=0;
	// parent(s)=-1;
	Enqueue(s,Q);
	While(Not IsEmptyQueue(Q)){
		v= Dequeue(Q);
		For each neighbor w of v {
			if(distance(w)== ∞){
				parent(w)=v;
				distance(w)=distance(v)+1;
				Enqueue(w,Q);
			}
		}
	}
	L-new adjacency list
	curr=t
	while(parent(curr)!=-1){
		add (parent(curr),curr) in L;
		curr=parent(curr);
	}
	return L;
}


Solve_Batman(G,M){
	k=BFS(G,s,t) //return shortest path length
	L=BFS_L(G,s,t) //return edges in shortest path

	For each (u,v) in E
	{
		M[u,v]=k;
		M[v,u]=k;
	}

	For each (u,v) in L
	{
		G=(V,E\{(u,v)}) //remove an edge
		len=BFS(G,s,t)
		M[u,v]=len;
		M[v,u]=len;
		G=(V,E) //add an edge 
	}
	return M;
}
-----------------------------------------------------
Min_cost(A){
	B=A;//copy of array A
	sort_inc(B); //sort in inc. order

	n=A.size();
	visited(n,0); // initially all postions unvisited
	Cost1=0;
	for( int i=0 ;i<n ; i++){
		if(!visited[i]){
			Cost1+= cost_calc(A,B,i,visited);
		}
	}

	C=A;//copy of array A
	sort_dec(C); //sort in dec. order

	visited2(n,0); // initially all postions unvisited
	Cost2=0;
	for( int i=0 ;i<n ; i++){
		if(!visited2[i]){
			Cost2+= cost_calc2(A,C,i,visited2);
		}
	}

	return min(Cost1,Cost2);
}

cost_calc(A,B,i,visited){
	mini= ∞ ;
	curr=i;
	Cost=0;
	while(visited[curr]!=1){
		visited[curr]=1;
		Cost+=A[curr];
		mini=min(mini,A[curr]);
		p = binary_search_inc_index(B,A[i]);
		curr=p;
	}
	return Cost-mini;
}
cost_calc2(A,C,i,visited){
	mini= ∞ ;
	curr=i;
	Cost=0;
	while(visited[curr]!=1){
		visited[curr]=1;
		Cost+=A[curr];
		mini=min(mini,A[curr]);
		p = binary_search_dec_index(C,A[i]);
		curr=p;
	}
	return Cost-mini;
}

// binary_search_inc_index-> returns index in increasing sorted array using binary search 
// binary_search_dec_index-> returns index in decreasing sorted array using binary search 

---------------------------------------------------
int M;// Money Shantanu initially has
int n; // no. of sweets
vector<int> sweets; // contain initial prices of sweets
int l,st;

if( n & (n-1) ){// if n is power of 2
	st= n;
}
else{
	st= 1<<(log2(n) + 1); 
}

l= 2*st - 1;
vector<int> A(l,0);

for(int i=0;i<n; i++){ // leaf nodes initialization
	A[st+i-1]=sweets[i];
}

for(int i =st-2;i>=0;i--){
	A[i]= A[2*i+1] + A[2*i+2];
}

update(i,x){
	i = i-1; //bring in 0-based indexing
	i = n-1 + i; //node position in tree
	int diff= x - A[i]; // amount of change

	A[i]=x; // update
	i = (i-1)/2;
	while(i>=0){
		A[i]+= diff;
		i = (i-1)/2;
	}
}

request(l,r){
	int i= l-1;j= r-1; //bring in 0-based indexing
	i = n-1 + i; //start node position in tree
	j = n-1 + j; //end node position in tree

	int sum=0; //stores purchase price of l to r
	if(i==j) sum= A[i];
	if(j>i){
		while( j>i ){
			if(i%2==0){
				sum+= A[i];
				i=i+1;
			}
			if(j%2==1){
				sum+= A[j];
				j=j-1;
			}

			i= (i-1)/2;
			j= (j-1)/2;
		}
		if(i==j) sum+= A[i];
	}

	if(sum<=M) cout<<"YES\n";
	else cout<<"NO\n";
}
------------------------------------
int n; // no. of rooms
int m; //no. of bombings
int len,st,l,r,c;
if( n & (n-1) ) st= n; // if n is power of 2
else st= 1<<(log2(n) + 1); 
len= 2*st - 1;
vector<int> A(l,-1);
vector<int> color_order(m);

for k=0 to m-1:{
	cin>>l>>r>>c;
	color_order[k]= c;

	i= l-1; j= r-1; //bring in 0-based indexing
	i = n-1 + i; //start node position in tree
	j = n-1 + j; //end node position in tree

	if(i==j) A[i]=k;
	else if(j>i){
		while( j>i ){
			if(i%2==0){
				A[i]=k;
				i=i+1;
			}
			if(j%2==1){
				A[j]=k;
				j=j-1;
			}

			i= (i-1)/2;
			j= (j-1)/2;
		}
		if(i==j) A[i]=k;
	}
}

vector<int> final_color(n);
for k=0 to n-1:{
	i = n-1 + k;
	last_color_index= -1;
	while(i>=0){
		last_color_index= max(last_color_index, A[i]);
		i = (i-1)/2;
	}
	final_color[k]= color_order[last_color_index];
}
------------------------------------------------
int s,d; // source and destination
tower_cities(n)// tower_cities[i]=1 if it has a tower else 0
g<- map/graph of state // adjacency list 

check_power(x){
	if(s==d) return true;
	vector<int> vis(n,-1);
	vis[s]=x;

	CreateEmptyQueue(Q);
	Enqueue(s,Q);
	While(Not IsEmptyQueue(Q)){
		v= Dequeue(Q);
		if(vis[v]==0) continue;
		For each neighbor w of v {
			if(vis[w]< vis[v]-1){
				vis[w]= vis[v]-1;
				if(tower_cities[w]) vis[w]=x;
				Enqueue(w,Q);
			}
		}
	}

	if(vis[d]!=-1)return true;
	else return false;
}

min_power(){
	int lo=0,hi=n;
	int mid= (lo+hi)>>1;
	int ans=n;

	while(lo<=hi){
		if(check_power(mid)){
			ans=mid;
			hi=mid-1;
		}
		else lo=mid+1;
		mid= (lo+hi)>>1;
	}
	return ans;
}
---------------------------------------
seq(n) //given seqn of size n
BFS(parent){
	CreateEmptyQueue(Q);
	Enqueue(1,Q);
	parent[1]=-1;

	While(Not IsEmptyQueue(Q)){
		v= Dequeue(Q);
		For each neighbor w of v {
			if(w!=parent[v]){
				parent[w]=v;
				Enqueue(w,Q);
			}
		}
	}
}
is_Edible(){
	parent(n+1); //stores parent of nodes in tree
	BFS(parent);
	if(seq[0]!=1)return false;

	CreateEmptyQueue(Q);
	Enqueue(1,Q);

	for( i=1 to n-1){
		while(Not IsEmptyQueue(Q) && parent[seq[i]] != Front(Q)){
			Dequeue(Q);
		}
		if(IsEmptyQueue(Q)) return false;
		else Enqueue(seq[i],Q);
	}
	return true;
}
------------------------------------