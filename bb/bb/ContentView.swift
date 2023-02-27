import SwiftUI
//import Firebase


//class AppDelegate: NSObject, UIApplicationDelegate {
//  func application(_ application: UIApplication,
//                   didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil) -> Bool {
//    FirebaseApp.configure()
//    return true
//  }
//}


struct ContentView: View {
    @State private var imageURLs = [String]()
    var body: some View {
        ZStack {
            LinearGradient(gradient: Gradient(colors: [.blue, .white]),
                           startPoint: .topLeading,
                           endPoint: .bottomTrailing)
            //.edgesIgnoringSafeArea[.all]
//        VStack {
//            HStack {
//                Text("Hello, User").foregroundColor(.white)
//                Button(action: {}){
//                    Text("Button")
//                }
//            }
            ScrollView {
                LazyVStack {
                    ForEach(imageURLs, id: \.self) { imageURL in
                        HStack {
                            Button(action: {
                                if let url = URL(string: imageURL) {
                                    UIApplication.shared.open(url)
                                }
                            }) {
                                Image("button-background")
                                    .resizable()
                                    .aspectRatio(contentMode: .fit)
                                    .frame(width: 40, height: 40)
                            }
                            Text("ProductX")
                                .foregroundColor(.white)
                                .font(.headline)
                                .padding(.leading)
                                .lineLimit(nil)
                        }
                        RemoteImage(url: imageURL)
                            .aspectRatio(contentMode: .fit)
                            .padding()
                            .onAppear(perform: {
                                // Load next set of images when the last image is visible
                                if imageURL == self.imageURLs.last {
                                    self.loadMoreImages()
                                }
                            })
                    }
                }
            }
//        }
        }
        .onAppear(perform: {
            // Load initial set of images
            self.loadMoreImages()
        })
    }
   
    private func loadMoreImages() {
        guard let url = URL(string: "http://129.21.61.27:4999/kappa") else { return }
       
        URLSession.shared.dataTask(with: url) { data, response, error in
            guard let data = data, error == nil else {
                print("Error: \(error?.localizedDescription ?? "Unknown error")")
                return
            }
           
            do {
                let jsonData = try JSONSerialization.jsonObject(with: data, options: []) as! [[Any]]
               print(jsonData)
                let newImageURLs = jsonData.compactMap { $0.last as? String }
               print(newImageURLs)
                DispatchQueue.main.async {
                    // Append new images to the existing list
                    self.imageURLs.append(contentsOf: newImageURLs)
                }
            } catch {
                print("Error parsing JSON: \(error.localizedDescription)")
            }
        }.resume()
    }
}


struct RemoteImage: View {
    @StateObject private var imageLoader = ImageLoader()
    private let url: String
   
    init(url: String) {
        self.url = url
    }
   
    var body: some View {
        if let image = imageLoader.image {
            Image(uiImage: image)
                .resizable()
        } else {
            Rectangle()
                .foregroundColor(.gray)
                .onAppear(perform: {
                    imageLoader.loadImage(from: url)
                })
        }
    }
}


class ImageLoader: ObservableObject {
    @Published var image: UIImage?
   
    func loadImage(from url: String) {
        guard let imageURL = URL(string: url) else { return }
       
        URLSession.shared.dataTask(with: imageURL) { data, response, error in
            guard let data = data, error == nil else {
                print("Error: \(error?.localizedDescription ?? "Unknown error")")
                return
            }
           
            DispatchQueue.main.async {
                self.image = UIImage(data: data)
            }
        }.resume()
    }
}


