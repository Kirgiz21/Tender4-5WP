from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Tender, TenderItem, Bidder, Bid, Award


# Tenders
class TenderListView(ListView):
    model = Tender
    template_name = 'tender_list.html'


class TenderDetailView(DetailView):
    model = Tender
    template_name = 'tender_detail.html'


class TenderCreateView(CreateView):
    model = Tender
    template_name = 'tender_form.html'
    fields = ['title', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('tenders')


class TenderUpdateView(UpdateView):
    model = Tender
    template_name = 'tender_form.html'
    fields = ['title', 'description', 'start_date', 'end_date']
    success_url = reverse_lazy('tenders')


class TenderDeleteView(DeleteView):
    model = Tender
    template_name = 'tender_confirm_delete.html'
    success_url = reverse_lazy('tenders')


# TenderItems
class TenderItemListView(ListView):
    model = TenderItem
    template_name = 'tender_item_list.html'

    def get_queryset(self):
        return TenderItem.objects.filter(tender_id=self.kwargs['tender_id'])


class TenderItemDetailView(DetailView):
    model = TenderItem
    template_name = 'tender_item_detail.html'


class TenderItemCreateView(CreateView):
    model = TenderItem
    template_name = 'tender_item_form.html'
    fields = ['name', 'description', 'quantity', 'unit']

    def form_valid(self, form):
        form.instance.tender_id = self.kwargs['tender_id']
        return super().form_valid(form)

    success_url = reverse_lazy('tenders')


class TenderItemUpdateView(UpdateView):
    model = TenderItem
    template_name = 'tender_item_form.html'
    fields = ['name', 'description', 'quantity', 'unit']
    success_url = reverse_lazy('tenders')


class TenderItemDeleteView(DeleteView):
    model = TenderItem
    template_name = 'tender_item_confirm_delete.html'
    success_url = reverse_lazy('tenders')


# Bidders
class BidderListView(ListView):
    model = Bidder
    template_name = 'bidder_list.html'


class BidderDetailView(DetailView):
    model = Bidder
    template_name = 'bidder_detail.html'


class BidderCreateView(CreateView):
    model = Bidder
    template_name = 'bidder_form.html'
    fields = ['name', 'contact_info']
    success_url = reverse_lazy('bidders')


class BidderUpdateView(UpdateView):
    model = Bidder
    template_name = 'bidder_form.html'
    fields = ['name', 'contact_info']
    success_url = reverse_lazy('bidders')


class BidderDeleteView(DeleteView):
    model = Bidder
    template_name = 'bidder_confirm_delete.html'
    success_url = reverse_lazy('bidders')


# Bids
class BidListView(ListView):
    model = Bid
    template_name = 'bid_list.html'

    def get_queryset(self):
        return Bid.objects.filter(tender_id=self.kwargs['tender_id'])


class BidDetailView(DetailView):
    model = Bid
    template_name = 'bid_detail.html'


class BidCreateView(CreateView):
    model = Bid
    template_name = 'bid_form.html'
    fields = ['bidder', 'price', 'terms']

    def form_valid(self, form):
        form.instance.tender_id = self.kwargs['tender_id']
        return super().form_valid(form)

    success_url = reverse_lazy('tenders')


class BidUpdateView(UpdateView):
    model = Bid
    template_name = 'bid_form.html'
    fields = ['bidder', 'price', 'terms']
    success_url = reverse_lazy('tenders')


class BidDeleteView(DeleteView):
    model = Bid
    template_name = 'bid_confirm_delete.html'
    success_url = reverse_lazy('tenders')


# Awards
class AwardListView(ListView):
    model = Award
    template_name = 'award_list.html'

    def get_queryset(self):
        return Award.objects.filter(tender_id=self.kwargs['tender_id'])


class AwardDetailView(DetailView):
    model = Award
    template_name = 'award_detail.html'


class AwardCreateView(CreateView):
    model = Award
    template_name = 'award_form.html'
    fields = ['bidder', 'price', 'terms']

    def form_valid(self, form):
        form.instance.tender_id = self.kwargs['tender_id']
        return super().form_valid(form)

    success_url = reverse_lazy('tenders')


class AwardUpdateView(UpdateView):
    model = Award
    template_name = 'award_form.html'
    fields = ['bidder', 'price', 'terms']
    success_url = reverse_lazy('tenders')


class AwardDeleteView(DeleteView):
    model = Award
    template_name = 'award_confirm_delete.html'
    success_url = reverse_lazy('tenders')
