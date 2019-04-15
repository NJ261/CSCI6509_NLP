child(john,mary). 
child(ann,john). 
child(tom,john). 
grandchild(C,G):-child(C,P),child(P,G).
