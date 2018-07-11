#include<stdio.h>
#include<stdlib.h>

struct btree
{
	int data;
	btree* right;
	btree* left;
};

btree* Insert(btree*,int data);
btree* getnewnode(int);
bool search(btree*,int data);

int main(int argc,char **argv){
	btree* root = NULL;
	root = Insert(root,10);
	root = Insert(root,14);
	root = Insert(root,27);
	root = Insert(root,9);
	root = Insert(root,67);
	root = Insert(root,55);
	search(root,atoi(argv[1]));
	return 0;	
}

btree* Insert(btree* root,int data)
{
	if(root == NULL){
		root = getnewnode(data);
		return root;
	}
	else if(data <= root->data){
		root->left = Insert(root->left,data);
	}
	else
	{
		root->right = Insert(root->right,data);	
	}
	return root;
}

btree* getnewnode(int data)
{
	btree* node = (btree*) malloc(sizeof(btree));
	node->data = data;
	node->left = node->right = NULL;
	return node; 
}

bool search(btree* root,int data){
	if(root == NULL){
		printf("NOT FOUND\n");
		return false;
	}
	else if(data == root->data){ 
		printf("FOUND\n");
		return true;
	}
	else if(data <= root->data){
		printf("going in left node\n");
		return search(root->left,data);
	}
	else{
		printf("going in right node\n");
		return search(root->right,data);
	}
}
