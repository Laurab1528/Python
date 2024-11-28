import json
from dictionary import CustomDict
from cost import CostDict
from order import WordForm

def main():
    
    with open('data.json', 'r') as f:
        data = json.load(f)

  
    d = CustomDict()
    for entry in data['dictionary_entries']:
        d.newentry(entry['key'], entry['value'])

    print("\nContenido del diccionario:")
    for key in d.dictionary:
        print(f"{key}: {d.looks(key)}")

  
    cost_dict = CostDict()
    total_cost_with_tax = cost_dict.get_total(data['cost_items'], data['tax_rate'])
    print(f"\nEl costo total con impuestos es: {total_cost_with_tax}")

   
    words = data['words_to_form']
    word_former = WordForm(words)
    formed_word = word_former.form_word()
    print(f"\nLa palabra formada es: {formed_word}")

if __name__ == "__main__":
    main()
