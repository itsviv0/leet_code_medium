/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* num1 = l1;   
    struct ListNode* num2 = l2;
    struct ListNode* sum_list = (struct ListNode*)malloc(sizeof(struct ListNode));
    sum_list->next = NULL;
    struct ListNode* cur = sum_list;
    int sum = 0, carry = 0, digit;
    while(num1!=NULL && num2!=NULL)
    {
        sum = num1->val + num2->val + carry;
        digit = sum % 10;
        carry = sum / 10;
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = digit;
        new_node->next = NULL;
        cur->next = new_node;
        cur = cur->next;
        num1 = num1->next;
        num2 = num2->next;
    }
    while(num1!=NULL)
    {
        sum = num1->val + carry;
        digit = sum % 10;
        carry = sum / 10;
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = digit;
        new_node->next = NULL;
        cur->next = new_node;
        cur = cur->next;
        num1 = num1->next;
    }
    while(num2!=NULL)
    {
        sum = num2->val + carry;
        digit = sum % 10;
        carry = sum / 10;
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = digit;
        new_node->next = NULL;
        cur->next = new_node;
        cur = cur->next;
        num2 = num2->next;
    } 
    if (carry != 0)
    {
        struct ListNode* new_node = (struct ListNode*)malloc(sizeof(struct ListNode));
        new_node->val = carry;
        new_node->next = NULL;
        cur->next = new_node;
        cur = cur->next;
    }
    return sum_list->next;   
}

// beats 83.17% runtime and 19.98% memrory
// https://leetcode.com/problems/add-two-numbers/submissions/1091116165/
