Rails.application.routes.draw do
  root to: 'pages#home'
  
  resources :blogs do
  	member do
  	  get :post_status
  	end
  end
end
