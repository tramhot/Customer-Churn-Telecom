from sklearn import metrics

def label(status):
    if status =='yes':
        return 1
    else:
        return 0
    
def print_stats(preds, target, sep='-', sep_len=40):
    target_names_list =['Stay', 'Go']
    accuracy = metrics.accuracy_score(target, preds)
    print('Accuracy = %.3f' % accuracy)
    print(sep*sep_len)
    print('Classification report:')
    classification_report = metrics.classification_report(target, preds, target_names= target_names_list)
    print(classification_report)
    print(sep*sep_len)
    print('Confusion matrix')
    cm=metrics.confusion_matrix(target, preds)
    print(cm)
    return accuracy, classification_report, cm