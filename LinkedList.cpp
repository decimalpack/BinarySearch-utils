class LLNode {
    public:
    int val;
    LLNode* next;
};

LLNode* reverseLL(LLNode* node) {
    LLNode *curr = node, *prev = nullptr, *tmp;
    while (curr) {
        tmp = curr->next;
        curr->next = prev;
        prev = curr;
        curr = tmp;
    }
    return prev;
}
LLNode* interleave(LLNode* a, LLNode* b) {
    LLNode *dummy = new LLNode(-1), *tmp = dummy;
    bool f = 1;
    while (a && b) {
        if (f) {
            tmp->next = a;
            a = a->next;
        } else {
            tmp->next = b;
            b = b->next;
        }
        tmp = tmp->next;
        f ^= 1;
    }
    tmp->next = a ? a : b;
    return dummy->next;
}
