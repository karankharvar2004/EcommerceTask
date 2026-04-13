from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Cart, CartItem, Order
from .serializers import ProductSerializer, CartSerializer, OrderSerializer
from django.shortcuts import get_object_or_404


class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all().order_by('-created_at')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()   # created_at auto added
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=204)


class AddToCart(APIView):

    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)
        cart_id = request.data.get('cart_id')

        if not product_id:
            return Response({"error": "product_id is required"}, status=400)

        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return Response({"error": "quantity must be a positive integer"}, status=400)

        if quantity <= 0:
            return Response({"error": "quantity must be a positive integer"}, status=400)

        product = get_object_or_404(Product, id=product_id)

        # Use an existing cart when provided, otherwise create a new one.
        if cart_id:
            cart = get_object_or_404(Cart, id=cart_id)
        else:
            cart = Cart.objects.create()

        # Check if item already exists
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        return Response({
            "message": "Added to cart",
            "cart_id": cart.id,
            "quantity": cart_item.quantity,
        })
    

class RemoveFromCart(APIView):

    def post(self, request):
        cart_id = request.data.get('cart_id')
        product_id = request.data.get('product_id')

        if not cart_id or not product_id:
            return Response(
                {"error": "cart_id and product_id required"},
                status=400
            )

        cart = get_object_or_404(Cart, id=cart_id)

        try:
            cart_item = CartItem.objects.get(
                cart=cart,
                product_id=product_id
            )

            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                return Response({"message": "Quantity decreased by 1"})
            else:
                cart_item.delete()
                return Response({"message": "Item removed from cart"})

        except CartItem.DoesNotExist:
            return Response(
                {"error": "Item not found in cart"},
                status=404
            )
        

class CartDetail(APIView):

    def get(self, request, pk):
        cart = get_object_or_404(Cart, id=pk)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class Checkout(APIView):

    def post(self, request):
        cart_id = request.data.get('cart_id')

        if not cart_id:
            return Response({"error": "cart_id is required"}, status=400)

        cart = get_object_or_404(Cart, id=cart_id)
        cart_items = cart.cartitem_set.all()

        if not cart_items.exists():
            return Response({"error": "Cart is empty"}, status=400)

        total = sum(item.product.price * item.quantity for item in cart_items)

        order = Order.objects.create(
            cart=cart,
            total_amount=total,
            is_paid=True
        )

        serializer = OrderSerializer(order)

        return Response(serializer.data)
