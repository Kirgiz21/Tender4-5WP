from django.urls import path
from . import views

urlpatterns = [
    path('', views.TenderListView.as_view(), name='tenders'),
    path('create/', views.TenderCreateView.as_view(), name='tender_create'),
    path('<int:pk>/', views.TenderDetailView.as_view(), name='tender'),
    path('<int:pk>/update/', views.TenderUpdateView.as_view(), name='tender_update'),
    path('<int:pk>/delete/', views.TenderDeleteView.as_view(), name='tender_delete'),

    path('<int:tender_id>/items/', views.TenderItemListView.as_view(), name='tender_items'),
    path('<int:tender_id>/items/create/', views.TenderItemCreateView.as_view(), name='tender_item_create'),
    path('items/<int:pk>/', views.TenderItemDetailView.as_view(), name='tender_item'),
    path('items/<int:pk>/update/', views.TenderItemUpdateView.as_view(), name='tender_item_update'),
    path('items/<int:pk>/delete/', views.TenderItemDeleteView.as_view(), name='tender_item_delete'),

    path('bidders/', views.BidderListView.as_view(), name='bidders'),
    path('bidders/create/', views.BidderCreateView.as_view(), name='bidder_create'),
    path('bidders/<int:pk>/', views.BidderDetailView.as_view(), name='bidder'),
    path('bidders/<int:pk>/update/', views.BidderUpdateView.as_view(), name='bidder_update'),
    path('bidders/<int:pk>/delete/', views.BidderDeleteView.as_view(), name='bidder_delete'),

    path('<int:tender_id>/bids/', views.BidListView.as_view(), name='bids'),
    path('<int:tender_id>/bids/create/', views.BidCreateView.as_view(), name='bid_create'),
    path('bids/<int:pk>/', views.BidDetailView.as_view(), name='bid'),
    path('bids/<int:pk>/update/', views.BidUpdateView.as_view(), name='bid_update'),
    path('bids/<int:pk>/delete/', views.BidDeleteView.as_view(), name='bid_delete'),

    path('<int:tender_id>/awards/', views.AwardListView.as_view(), name='awards'),
    path('<int:tender_id>/awards/create/', views.AwardCreateView.as_view(), name='award_create'),
    path('awards/<int:pk>/', views.AwardDetailView.as_view(), name='award'),
    path('awards/<int:pk>/update/', views.AwardUpdateView.as_view(), name='award_update'),
    path('awards/<int:pk>/delete/', views.AwardDeleteView.as_view(), name='award_delete'),
]