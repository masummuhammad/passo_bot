
from add_best_seats_to_basket import add_best_seats_to_basket
from clear_basket import clear_basket
from get_available_block_list import get_available_block_list
from get_event_id import get_event_id
from get_event_details import get_event_details
from get_new_token import get_new_token, check_token_validity
from get_user_basket_info import get_user_basket_booking
from seat_category_variant_id import get_variants
from priority_validation_rule import priority_validation_rule
from settings import *
from tanimla import tanimla
from initdb import initdb
#########################################
#db
import sqlite3
connection=sqlite3.connect('DB2.db')
c=connection.cursor()
c.execute('select email from current_user')

current_email=c.fetchall()[0]

print("Current user is : %s"%current_email)
c.execute("select * from user_data where email='%s';"%current_email)
d=c.fetchall()[0]
#('batunal1415@gmail.com', 'Mustafa3434', 'Galatasaray A.S', 1, 4, 2, '35234', 'can eker', '4526454', '3', '2523', '345')

email=d[0]
password=d[1]
event_name=d[2]

quantity=d[3]
category_id=d[4]
priority_display_serial=d[5]
priority1_display_value=d[6]
name=d[7]
cardnumber=d[8]
cardexpiredatemonth=d[9]
cardexpiredateyear=d[10]
cardcvv2=d[11]


###########################################

initdb(email,password)

def main(event_name,email,password,priority_display_serial,name,cardnumber,cardexpiredatemonth,cardexpiredateyear,cardcvv2,MAX_NUMBER_OF_TICKET_IN_BASKET,category_id):
    done: bool
    found_ticket_total_number: int = 0
    print("Checking token validity...")
    valid = check_token_validity(email)
    
    if valid == 'invalid':
        print("Getting new token...")
        get_new_token(email,password)
    elif valid == 'valid':
        print("Clearing basket...")
        clear_basket(email)
    elif valid == 'new_otp_required':
        return
    print("Get event id...")
    event_id = get_event_id(event_name,email)
    
    if event_id == "no_event":
        done = True
        return done
    print("Getting event details...")
    event_details = get_event_details(event_id[0],event_id[1])
    
    event_priority_details = event_details[1]
    
    if len(event_priority_details) != 0:
        for serial in range(0, len(event_priority_details)):
            if priority_display_serial == serial + 1:
                ValidationIntegrationID = event_priority_details[serial]['id']
                print("Validating priority...")
                priority_validation_rule(event_id[0], ValidationIntegrationID, priority1_display_value,email)

    seat_category_id_list = event_details[0]

    
    if len(seat_category_id_list) < category_id:
        print("Failed to find out this category. It's gonna try again... ")
        print("Retrying...")    
        done = False
        return done
    
    max_ticket_found: bool = False
    try_number = 0
    while max_ticket_found is False:
        seat_category_id = seat_category_id_list[category_id - 1]["id"]
        print("Getting variants ...")
        variants_id = get_variants(event_id[0], seat_category_id,email)
        print("Getting available block list...")
        block_ids = get_available_block_list(event_id[0], seat_category_id,email,password)
        if len(block_ids)==0:
            continue
            
        print(f"Number of available blocks: {len(block_ids)}")

        block_ids.reverse()
        
        for block_id_ in block_ids:
            block_id = block_id_["id"]
            block_name = block_id_["name"]
            print("Trying to add best seats to basket...")
            found_ticket_total_number = add_best_seats_to_basket(block_name, block_id, event_id[0], seat_category_id, variants_id, MAX_NUMBER_OF_TICKET_IN_BASKET, found_ticket_total_number,email,password)
            if found_ticket_total_number == 'try_next_block':
                continue
            if found_ticket_total_number == 'max_ticket_in_basket':
                break
            if MAX_NUMBER_OF_TICKET_IN_BASKET <= found_ticket_total_number:
                print(">>Maximum  ticket  added to basket for this event.<<")
                print('_'*30)
                break
        user_basket_info_ = get_user_basket_booking(email)
        if user_basket_info_=='empty_basket':
            continue
        
        row_ids = []
        for row_id in user_basket_info_:
            if len(row_ids) <= MAX_NUMBER_OF_TICKET_IN_BASKET:
                row_ids.append(row_id['rowId'])
        
           
        print(f"{len(row_ids)} ticket(s) added to basket.")
        
        
        tanimla_status = tanimla(row_ids, event_id[0],email,password,name,cardnumber,cardexpiredatemonth,cardexpiredateyear,cardcvv2)
    
        if tanimla_status == 'done':
            print("Ticket purchased successfully")
            return True
        if tanimla_status == 'error':
            print("Failed to purchase ticket")
            return 'error'
        if MAX_NUMBER_OF_TICKET_IN_BASKET <= len(user_basket_info_):
            max_ticket_found = True
        else:
            try_number += 1
            print(f"{try_number}: {len(user_basket_info_)} ticket found, trying again for new block")
            continue
        if max_ticket_found:
            done = True
            return done


if __name__ == '__main__':
    main_while = True
    
    while main_while:
        try:
            ticket_added = main(event_name,email,password,priority_display_serial,name,cardnumber,cardexpiredatemonth,cardexpiredateyear,cardcvv2,quantity,category_id)
            if ticket_added:
                main_while = False
        except Exception as e:
            print(e)
connection.close()