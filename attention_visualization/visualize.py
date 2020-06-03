def attention2color(attention_score):
    r = 255 - int(attention_score * 255)
    color = rgb_to_hex((255, r, r))
    return str(color)

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

from IPython.core.display import display, HTML


def visualize_attention(model_att,model, text, price, tokenizer):
    
    #idx = np.random.randint(low = 0, high=X_te.shape[0]) # Get a random test
    tokenized_sample = tokenize(tokenizer, text) # Get the tokenized text
    #print('tokenized_sample :', tokenized_sample)
    _, attentions = model_att.predict(tokenized_sample) # Perform the prediction
    label_probs = model.predict([tokenized_sample,np.array(price)])
    
    #print('label_probs :', label_probs)
    #print('attentions :', attentions.shape)
    #global attentions0
    #attentions0 = attentions
    
    attentions = attentions.mean(axis=1)
    # Get decoded text and labels
    tokenized_sample = list(tokenized_sample)[0]
    #print('tokenized_sample :', tokenized_sample)
    id2word = dict(map(reversed, tokenizer.vocab.items()))
    decoded_text = [id2word[word] for word in tokenized_sample] 
    
    #print('decoded_text :', decoded_text)
    
    # Get classification
    label = np.argmax(label_probs, axis=1)[0] # Only one
    label2id = ['AC/ REFRIGERATION', 'ACCS. FOR FILTER BAG',
       'ADHESIVES & SEALANTS', 'ANALYSER', 'AUTO ELECTRICAL',
       'AUTOMOBILE SPARES', 'BALL MILL LINERS', 'BEARING',
       'BELT CONV-CHN&SPARES', 'BELT CONV-IDLERS', 'BELT CONVEYORS',
       'BLOWERS & FANS', 'BOLT', 'BULLDOZER', 'CABLE GLANDS',
       'CABLE LUGS', 'CABLES & ACCESSORIES', 'CASTING', 'CHN/SCRW/DBC/BE',
       'COLD VULCAN SOLN', 'COMPRESSORS', 'COMPUTER & ACESSORIE',
       'COOLING TOWER', 'COUPLING', 'CPP', 'CRANE', 'DESALINATION PLANT',
       'DG SET', 'DRILLING EQUIPMENTS', 'DUMPERS/VOLVO TIPPER',
       "E'TRICAL HOIST/ LIFT", "E'TRICAL MOTORS", 'ELECTRICAL GENERAL',
       'ENGINES (DIESEL)', 'ESP', 'EXCAVATOR', 'EXPLOSIVES',
       "FIELD INSTRUMENT'N", 'FILTER BAGS  NONWOV.', 'FK PNEUMATIC PUMPS',
       'FORK LIFT', 'FURNITURE & FIXTURES', 'GEAR BOX', 'GEARED MOTOR',
       'GENERAL CONSUMABLES', 'GI / GALV SHT/ ITEMS', 'GRATINGS',
       'HARDWARE', 'HEMM SPARES', 'HRCS CASTING', 'INSTRUMENTATION',
       'JETTY', 'LABORATORY EQUIPMENT', 'LIGHTING FIXTURES',
       'LOCOMOTIVES', 'LOTO DEVICE', 'MCC & PCC', 'MECHANICAL GENERAL',
       'METALLIC ANCHORS', 'MGRADER', 'MINES GENERAL', 'MTPS ITEMS',
       'NON FERROUS', 'NON-STOCK ITEMS', 'OIL & LUBRICANTS',
       'OTHREFRACTORY ITEMS', 'PACKING & SEALS', 'PAINTS & VARNISH',
       'PANEL CONTROL SUBSYS', 'PAY LOADER', 'PIPE & PIPE FITTINGS',
       'PLC,DCS&LVM SYSTEMS', 'PNEUMATIC&HYDRAULIC', 'POWER ELECTRONICS',
       "POWER TRANSM'N UNIT", 'PP BAGS', 'PROJECT ITEMS',
       'PUBLIC ADDRESSING', 'RAILWAY ITEMS', 'REF. ALUMINA BRICKS',
       'REF. IMPORTED BRICKS', 'RETREADED TYRE', 'ROAD SWEEPING M/C',
       'ROBOTICS', 'ROCK BREAKER', 'SAFETY GOGGLES', 'SAFETY HANDGLOVES',
       'SAFETY ITEMS', 'SAFETY SHOES', 'SANITORY & BUILDING',
       'SPARES FOR BEARINGS', 'SPRS / GRR / GRS', 'STATIONARY ITEMS',
       'STEEL', 'STEEL - PLATE', 'SURFACE MINE', 'SWITCH GEAR - 6.6 KV',
       'SWITCH YARD -132/220', 'TELEPHONE & TELECOMM',
       'THERMAL POWER PLANT', 'TIPPLERS - WAGON', 'TOOLS & TACKLES',
       'TRANSFORMER', 'TYRES AND TUBES', 'UTILITY SERVICES', 'V-BELT',
       'WATERPUMP /TREATMENT', 'WEIGHING SYSTEMS', 'WELDING MATERIALS',
       'WELFARE ITEMS', 'WHRU', 'WINDING & INSULATING',
       'WORKSHOP M/C SPARES']
    
    print("label :", label2id[label])

    # Get word attentions using attenion vector
    token_attention_dic = {}
    max_score = 0.0
    min_score = 0.0
    
    attentions_text = attentions[0,-len(tokenized_sample):]
    
    #print('decoded_text :', attentions_text)
    #plt.bar(np.arange(0,len(attentions.squeeze())), attentions.squeeze())
    #plt.show();
    #print(attentions_text)
    attentions_text = (attentions_text - np.min(attentions_text)) / (np.max(attentions_text) - np.min(attentions_text))
    for token, attention_score in zip(decoded_text, attentions_text):
        #print(token, attention_score)
        token_attention_dic[token] = attention_score
        
    #print('token_attention_dic :', token_attention_dic)
        

    # Build HTML String to viualize attentions
    html_text = "<hr><p style='font-size: large'><b>Text:  </b>"
    for token, attention in token_attention_dic.items():
        #print('token :', token)
        #print('attention :', attention)
        #attention = np.mean(attention)
        #print('attention :', attention)
        html_text += "<span style='background-color:{};'>{} <span> ".format(attention2color(attention),
                                                                            token)
    #html_text += "</p><br>"
    #html_text += "<p style='font-size: large'><b>Classified as:</b> "
    #html_text += label2id[label] 
    #html_text += "</p>"
    
    # Display text enriched with attention scores 
    display(HTML(html_text))