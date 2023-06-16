#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount = 0, total = 0, items=None, last_item_price = 0):
    self.discount = discount
    self.total = total
    self.items = items if items is not None else []
    self.last_item_price = last_item_price

  
  def add_item(self, title, price, quantity = 1):
    self.total += price * quantity
    i=0
    self.last_item_price = price * quantity
    while i < quantity:
      self.items.append(title)
      i+=1

    
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.discount*10
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.last_item_price
