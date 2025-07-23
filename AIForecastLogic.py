def stock_forecaster(data, context):
    sale = data['value']
    product_id = sale['productID']
    
    sales_ref = db.collection('sales')
    last_week_sales = sales_ref \
        .where('productID', '==', product_id) \
        .order_by('timestamp', direction='DESCENDING') \
        .limit(7) \
        .get()
    
    total_sales = sum([s.quantity for s in last_week_sales])
    
    demand_multiplier = 2.5 if typhoon_alert_active() else 1.0
    daily_demand = (total_sales / 7) * demand_multiplier
    
    product_ref = db.collection('products').document(product_id)
    current_stock = product_ref.get().to_dict()['currentStock']
    
    product_ref.update({
        'forecast': {
            'dailyDemand': daily_demand,
            'daysUntilStockout': current_stock / daily_demand
        }
    })
    
    if (current_stock / daily_demand) < product_ref.get().to_dict()['minStockThreshold']:
        create_alert(product_id, current_stock)
